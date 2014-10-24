__author__ = 'jacobritenour'

'''
Jacob Ritenour
10-16-2014
DPFWP
Reusable Library Assignment
'''
import webapp2 #how do I get this?
from lib import CarData, FavoriteCars # importing from the other 2 py pages
from page import ResultsPage, FormPage #importing to report the results



class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for form
        f = FormPage()


        #page for class
        p = ResultsPage()

        p.body = fmlib.compile_list() + fmlib.calc_time_span() #to show the given info plus the added utility
        self.response.write(p.print_out())# print all

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)