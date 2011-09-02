# -*- coding : utf-8 -*-

from gpipes import utils


class RssFeedPublisher(object):
    def __init__(self, config, environ):
        self.pipeline_name = environ["pipeline_name"]
        self.title = config.get("title", "Gpipes rss")
        self.link = config.get("link", "http://localhost/")
        self.description = config.get("description", "Gpipes rss")

    def _save_feed(self, feed):
        from gpipes import models
        from google.appengine.ext import db
        key_name = models.Feed.create_key_name(self.pipeline_name)
        new_feed = models.Feed.get_or_insert(key_name)
        def txt():
            new_feed.name = utils.to_unicode(self.title)
            new_feed.url = utils.to_unicode(self.link)
            new_feed.content = utils.to_unicode(feed.writeString("utf-8"))
            new_feed.format = utils.to_unicode("application/xml;charset=UTF-8")
            new_feed.put()
        db.run_in_transaction(txt)

    def _create_feed(self, content):
        from django.utils import feedgenerator

        feed = feedgenerator.Rss201rev2Feed(
            title = self.title,
            link = self.link,
            description = self.description,
            language = u'ja'
            )

        for entry in content["entries"]:
            feed.add_item(
                title = entry["title"],
                link = entry["link"],
                description = utils.get_summary(entry),
                pubdate = utils.get_updated(entry),
                )

        return feed

    def execute(self, content):
        feed = self._create_feed(content)
        self._save_feed(feed)
        return content


def create(config, environ):
    return RssFeedPublisher(config, environ)

