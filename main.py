import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
import json

from tornado.options import define, options
define("port", default=6010, help="run on the given port", type=int)
define("debug", default=0, help="1:watch in real time (debug mode)", type=bool)

class Application(tornado.web.Application):
    def __init__(self):
        conn = pymongo.Connection("localhost", 27017)
        self.db = conn.mensa

        handlers=[
            (r'/', IndexHandler),
            (r'/mensa/v1/today/', MensaHandler)
            ]
        tornado.web.Application.__init__(self, handlers, debug=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

class MensaHandler(tornado.web.RequestHandler):
    def get(self):
        db = self.application.db
        item = db.mensa.menu.find_one({"date":"13.12.2013"})
        self.write("{ \
                date:"+item['date']+", \
        menu1:{name:"+item['menu1']['name']+", image:"+item['menu1']['image']+"}, \
        menu2:{name:"+item['menu2']['name']+", image:"+item['menu2']['image']+"} \
        }")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
