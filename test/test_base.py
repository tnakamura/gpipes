#!/usr/bin/env python
#encoding: utf-8

import os
import sys

GAE_HOME = 'C:/google_appengine'
PROJECT_HOME = os.path.join(GAE_HOME, 'apps', 'gpipes', 'src')

EXTRA_PATHS = [
    GAE_HOME,
    PROJECT_HOME,
    os.path.join(GAE_HOME, 'google', 'appengine', 'api'),
    os.path.join(GAE_HOME, 'google', 'appengine', 'ext'),
    os.path.join(GAE_HOME, 'lib', 'yaml', 'lib'),
    os.path.join(GAE_HOME, 'lib', 'webob'),
    os.path.join(GAE_HOME, 'lib', 'django'),
]

sys.path = EXTRA_PATHS + sys.path


import unittest


from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import urlfetch_stub
from google.appengine.api import user_service_stub
from google.appengine.api import users
from google.appengine.ext import db


APP_ID = u"test_id"
AUTH_DOMAIN = "gmail.com"
LOGGED_IN_USER = "test@example.com"


class GAETestBase(unittest.TestCase):
    def setUp(self):
        # Regist API Proxy
        apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()

        # Regist Datastore stub
        stub = datastore_file_stub.DatastoreFileStub(APP_ID,
                '/dev/null',
                '/dev/null')
        apiproxy_stub_map.apiproxy.RegisterStub("datastore_v3", stub)
        os.environ["APPLICATION_ID"] = APP_ID

        # Regist UserService stub
        apiproxy_stub_map.apiproxy.RegisterStub("user",
                user_service_stub.UserServiceStub())
        os.environ["AUTH_DOMAIN"] = AUTH_DOMAIN
        os.environ["USER_EMAIL"] = LOGGED_IN_USER
        
        # Regist urlfetch stub
        apiproxy_stub_map.apiproxy.RegisterStub('urlfetch',
                urlfetch_stub.URLFetchServiceStub())
        
        # Regist MailService stub
        apiproxy_stub_map.apiproxy.RegisterStub('mail',
               mail_stub.MailServiceStub()) 

