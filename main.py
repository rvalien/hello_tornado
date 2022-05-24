import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class CompareHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>compare with fast-api <a href='https://codeahoy.com/compare/tornado-vs-fastapi'>here</a></h1>")


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = 'hot ☀️' if degree > 20 else 'cold ⛄'
        drink = 'have some Beer 🍺️' if degree > 20 else 'you need hot beverage ☕'
        self.render('weather.html', output=output, drink=drink)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        ("/compare", CompareHandler),
        ("/home", HomeHandler),
        ("/weather", WeatherHandler),
    ],
        debug=True,
        autoreload=True,
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
