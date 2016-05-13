#!/usr/bin/env python
import tornado.web
import tornado.httpserver
import tornado.auth
import tornado.ioloop

class TwitterHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        oAuthToken = self.get_secure_cookie("oauth_token")
        oAuthSecret = self.get_secure_cookie("oauth_secret")
        userID = self.get_secure_cookie("user_id")

        if self.get_