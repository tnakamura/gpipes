# -*- coding : utf-8 -*-

class ReadMoreFilter(object):
    def __init__(self, config, environ):
        pass

    def execute(self, content):
        for entry in content["entries"]:
            tag = '<p><a href="%s" target="_blank">Read more...</a></p>' % entry["link"]
            detail = entry.get("summary_detail", None)
            if detail:
                entry["summary_detail"]["value"] = detail["value"] + tag
            else:
                entry["summary"] = entry.get("summary", "") + tag

        return content


def create(config, environ):
    return ReadMoreFilter(config, environ)

