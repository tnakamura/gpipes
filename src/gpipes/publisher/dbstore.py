# -*- coding : utf-8 -*-

class DatastorePublisher(object):

    def __init__(self, config, environ):
        self.pipeline_name = environ["pipeline_name"]

    def execute(self, content):
        from google.appengine.ext import db
        from gpipes import utils
        from gpipes import models

        feed_key_name = models.Feed.create_key_name(self.pipeline_name)
        feed = models.Feed.get_or_insert(feed_key_name)

        entries = []
        for entry in content["entries"]:
            key_name = models.Entry.create_key_name(self.pipeline_name, entry["link"])
            e = models.Entry.get_or_insert(key_name, parent=feed)
            e.pipeline = self.pipeline_name
            e.title = entry["title"]
            e.url = entry["link"]
            e.summary = utils.get_summary(entry)
            e.updated = utils.get_updated(entry)
            entries.append(e)

        def txt():
            db.put(entries)
        db.run_in_transaction(txt)

        return content


def create(config, environ):
    return DatastorePublisher(config, environ)

