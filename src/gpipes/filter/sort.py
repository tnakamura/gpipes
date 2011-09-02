# -*- coding : utf-8 -*-

class SortFilter(object):
    def __init__(self, config, environ):
        self.reverse = config.get("reverse", False)
        self.key = config.get("key", "updated_parsed")

    def execute(self, content):
        def getkey(a):
            return a[self.key]
        content.get("entries", []).sort(key=getkey, reverse=self.reverse)
        return content

def create(config, environ):
    return SortFilter(config, environ)

