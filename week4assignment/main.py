'''
Jacob Ritenour
10/21/2014
DPFWP
Week 4 Assignment Dynamic Site
'''
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        p = Page

        print

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
