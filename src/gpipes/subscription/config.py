# -*- coding : utf-8 -*-

class Config(object):
    def __init__(self, config, environ):
        self.feeds = config.setdefault("feed", [])

    def execute(self, content=None):
        import feedparser
        from google.appengine.api import urlfetch
 
        for url in self.feeds:
            result = urlfetch.fetch(url=url, deadline=10)
            d = feedparser.parse(result.content)
            if not content:
                content = d
            else:
                if not content.has_key("feed"):
                    content["feed"] = d.feed
                entries = content.setdefault("entries", [])
                entries.extend(d.entries)
                content["entries"] = entries

        return content


def create(config, environ):
    return Config(config, environ)

