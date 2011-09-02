# -*- coding : utf-8 -*-
import logging


from gpipes import utils


class PipelineError(Exception):
    pass


class PipelineManager(object):
    def __init__(self, config_path):
        import yaml
        config = yaml.safe_load(open(config_path, "r"))
        self.environ = config.get("global", {})
        self.configs = config.get("pipeline", [])

    def run(self, pipeline_name):
        plugins = self.create_plugins(pipeline_name)
        self.try_run_next(plugins, {})
    
    def try_run_next(self, plugins, content):
        if 0 < len(plugins):
            from google.appengine.ext import deferred
            deferred.defer(self.execute_plugin, plugins, content)

    def execute_plugin(self, plugins, content):
        plugin = plugins.pop(0)
        result = plugin.execute(content)
        self.try_run_next(plugins, result)

    @utils.memoize
    def create_plugins(self, pipeline_name):
        if not pipeline_name in self.configs:
            raise PipelineError("pipeline '%s' not found in gpipes.cfg." % pipeline_name)
        plugin_configs = self.configs[pipeline_name]
        logging.info("plugin count: %s" % len(plugin_configs))

        environ = self.environ.copy()
        environ["pipeline_name"] = pipeline_name

        return [self.create_plugin(module_node, environ)\
            for module_node in plugin_configs]

    def create_plugin(self, module_node, environ):
        # Load plugin module.
        module_name = module_node["module"]
        module = self.import_from_string(module_name)

        # Create plugin instance
        create = getattr(module, "create")
        config = module_node.setdefault("config", {})
        return create(config, environ)

    def import_from_string(self, name):
        mod = __import__(name, globals(), locals(), [], -1)
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

