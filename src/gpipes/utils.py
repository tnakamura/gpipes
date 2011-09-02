# -*- coding : utf-8 -*-

import time
import hashlib


from datetime import datetime


def memoize(original_func):
    cache = {}
    def decorated_func(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = original_func(*args)
            return cache[args]
    return decorated_func


def get_summary(entry):
    detail = entry.get("summary_detail", None)
    if detail:
        return detail["value"]
    else:
        return entry.get("summary", "")


def get_updated(entry):
    if entry.has_key("updated_parsed"):
        tm = time.mktime(entry["updated_parsed"])
        return datetime.fromtimestamp(tm)
    else:
        return datetime.now()


def to_unicode(s):
    if isinstance(s, unicode):
        return s
    else:
        return s.decode("utf-8")


def merge_result(content, sub_modules, arg = None):
    if not isinstance(content, list):
        content = [content]

    for module in sub_modules:
        result = module.execute(arg)
        if not result:
            pass
        elif not isinstance(result, list):
            content.append(result)
        else:
            content.extend(result)

    return content

