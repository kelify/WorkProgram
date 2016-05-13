#!/usr/bin/env python
import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        # UserAgent = self.request
        # print UserAgent.headers["Cookie"]
        count = int(cookie) + 1 if cookie else 1
        countString = "1 time" if count == 1 else "%d times"%count

        self.set_secure_cookie("count", str(count))
        self.write(
            """
            <html>
            <head><title>Cookie Counter</title></head>
            <body><h1>You are viewed this page %s times.</h1>
            </body>
            </html>
            """%countString
        )
if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "cookie_secret":"bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
    }
    application = tornado.web.Application(
        handlers=[(r'/', MainHandler)],
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()