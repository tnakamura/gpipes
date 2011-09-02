# -*- coding : utf-8 -*-
#!/usr/bin/env python


import os
import logging


from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util


import gpipes
from gpipes import models


class BaseHandler(webapp.RequestHandler):
    def handle_exception(self, exception, debug_mode):
        logging.exception(exception)
        super(BaseHandler, self).handle_exception(exception, debug_mode)

    def create_manager(self):
        path = os.path.join(os.path.dirname(__file__), "gpipes.cfg")
        return gpipes.PipelineManager(path)


class MainHandler(BaseHandler):
    # admin only
    def get(self):
        manager = self.create_manager()
        path = os.path.join(os.path.dirname(__file__), "index.html")
        values = {
                "pipelines": manager.configs,
                }
        self.response.out.write(template.render(path, values))


class PipelineHandler(BaseHandler):
    # admin only
    def get(self, name):
        manager = self.create_manager()
        manager.run(name)
    

class FeedHandler(BaseHandler):
    def get(self, name):
        feed = models.Feed.get_by_pipeline_name(name)
        if not feed or not feed.content:
            self.error(404)
            return
        self.response.headers["Content-Type"] = feed.format
        self.response.out.write(feed.content)


def main():
    application = webapp.WSGIApplication([
        ('/', MainHandler),
        ('/result/(.*)', FeedHandler),
        ('/(.*)', PipelineHandler),
        ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

