__author__ = 'jacobritenour'


import webapp2
from lib import CarData, FavoriteCars
from page import FormPage, ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for form
        f = FormPage()

        #page for class
        p = ResultsPage()
        fmlib = FavoriteCars()

        md1 = CarData()#calling the class
        md1.title = "The Princess Bride"
        md1.year = 1989 #going to call a function
        md1.director = "Rob Reiner"
        fmlib.add_car(md1)

        md2 = CarData()#calling the class
        md2.title = "Dune"
        md2.year = 1986 #going to call a function
        md2.director = "David Lynch"
        fmlib.add_car(md2)

       #movie title
        #year movie was made
        #director of the film

        p.body = fmlib.compile_list() + fmlib.calc_time_span()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)