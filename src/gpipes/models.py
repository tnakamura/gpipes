# -*- coding : utf-8 -*-

from google.appengine.ext import db

class Feed(db.Model):
    url = db.StringProperty()
    name = db.StringProperty()
    format = db.StringProperty(default="text/xml")
    content = db.TextProperty()

    @classmethod
    def create_key_name(cls, pipeline_name):
        return "p=%s;" % pipeline_name

    @classmethod
    def get_by_pipeline_name(cls, pipeline_name):
        key_name = cls.create_key_name(pipeline_name)
        return Feed.get_by_key_name(key_name)


class Entry(db.Model):
    pipeline = db.StringProperty()
    url = db.StringProperty()
    title = db.StringProperty()
    updated = db.DateTimeProperty(auto_now_add=True)
    summary = db.TextProperty()
    author = db.StringProperty()

    @classmethod
    def create_key_name(cls, pipeline_name, url):
        return "p=%s;e=%s;" % (pipeline_name, url)


