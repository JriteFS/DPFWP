'''
Jacob Ritenour
10/21/2014
DPFWP
Week 4 Assignment Dynamic Site
'''
import webapp2
from pages import Page
from data import DataObject, Data


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()# created instance of Page
        do = DataObject() #created instance of Data Object
        d = Data()

        p.data = d.werewolf.name

        self.response.write(p.print_initial())
        #self.response.write(p.print_types())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
