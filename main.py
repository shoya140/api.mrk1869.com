import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=6010, help="run on the given port", type=int)
define("debug", default=0, help="1:watch in real time (debug mode)", type=bool)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print "Hello, World"

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        debug=options.debug,
        handlers=[(r'/', IndexHandler)],
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
