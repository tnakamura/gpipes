# -*- coding : utf-8 -*-

from gpipes import models

class UnreadFilter(object):
    def __init__(self, conifg, environ):
        self.pipeline_name = environ["pipeline_name"]

    def check(self, link, updated, feed):
        from gpipes import utils
        key_name = models.Entry.create_key_name(self.pipeline_name, link)
        entry = models.Entry.get_by_key_name(key_name, parent=feed)
        if not entry:
            return False
        elif updated and entry.updated.timetuple()[:6] < updated[:6]:
            return False
        else:
            return True

    def execute(self, content):
        feed_key_name = models.Feed.create_key_name(self.pipeline_name)
        feed = models.Feed.get_or_insert(feed_key_name)
        
        entries = []
        for entry in content["entries"]:
            link = entry["link"]
            updated = entry.get("updated_parsed", None)
            if not self.check(link, updated, feed):
                entries.append(entry)
        content["entries"] = entries

        return content


def create(config, environ):
    return UnreadFilter(config, environ)

