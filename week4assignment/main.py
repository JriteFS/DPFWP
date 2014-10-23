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

        p = Page()# created instance of Page
        self.response.write(p.print_initial())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
