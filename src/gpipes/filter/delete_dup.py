# -*- coding : utf-8 -*-

class DeleteDuplicatedLinkFilter(object):
    def __init__(self, config, environ):
        pass

    def execute(self, content):
        check_link = {}
        def check(e):
            check_link[e["link"]] = 1
            return e

        content["entries"] = [
            check(e)
            for e in content["entries"]
            if not check_link.get(e["link"], 0)
            ]
        return content


def create(config, environ):
    return DeleteDuplicatedLinkFilter(config, environ)

