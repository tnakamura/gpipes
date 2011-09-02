class GrepFilter(object):
    def __init__(self, config, environ):
        self.key = config.get("key")
        self.pattern = config.get("pattern")
        self.exclusive = config.get("exclusive", False)

    def execute(self, content):
        import re
        prog = re.compile(self.pattern, re.MULTILINE)

        matches = []
        unmatches = []
        for entry in content.get("entries", []):
            if prog.match(entry[self.key]):
                matches.append(entry)
            else:
                unmatches.append(entry)

        if self.exclusive:
            content["entries"] = unmatches
        else:
            content["entries"] = matches

        return content


def create(config, environ):
    return GrepFilter(config, environ)

