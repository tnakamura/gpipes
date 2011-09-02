# -*- coding : utf-8 -*-

class XmlRpcPublisher(object):
    def __init__(self, config, environ):
        self.blog_id = config.get("blog_id", "MyBlog")
        self.api_url = config["api_url"]
        self.username = config["username"]
        self.password = config["password"]

    def execute(self, content):
        import xmlrpclib
        from gpipes import utils
        server = xmlrpclib.Server(self.api_url)
        for entry in content["entries"]:
            server.metaWeblog.newPost(
                    self.blog_id,
                    self.username,
                    self.password,
                    {
                        "title": entry["title"],
                        "description": utils.get_summary(entry),
                    },
                    xmlrpclib.True)
        return content


def create(config, environ):
    return XmlRpcPublisher(config, environ)

