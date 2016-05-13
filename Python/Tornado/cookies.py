#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os.path
import tornado.options

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class BseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BseHandler):
    def get(self):
        self.render("login.xhtml")

    def post(self):
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect("/")

class WelcomeHandler(BseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("Cookie_index.xhtml", user=self.current_user)

class LogoutHandler(BseHandler):
    def get(self):
        if (self.get_argument("logout",None)):
            self.clear_cookie("username")
            self.redirect("/")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "template_path":os.path.join(os.path.dirname(__file__), "templates"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "xsrf_cookies":True,
        "login_url":"/login"
    }
    application = tornado.web.Application(
        handlers=[
            (r'/', WelcomeHandler),
            (r'/login', LoginHandler),
            (r'/logout',LogoutHandler)
                  ],
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()