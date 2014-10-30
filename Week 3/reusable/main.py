__author__ = 'jacobritenour'

'''
Jacob Ritenour
10-16-2014
DPFWP
Reusable Library Assignment
'''
import webapp2 #how do I get this?
from page import ResultsPage, FormPage #importing to report the results
from lib import FavoriteCars, CarData



class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for form
        f = FormPage()

       # f.fmlib()

        #page for class
        p = ResultsPage()

        fmlib = FavoriteCars()

        cd = CarData()#calling car data info

        if self.request.GET:
            #stores info that came from the form to be used later
            cd.make = self.request.GET['make']#add this to the array
            cd.model = self.request.GET['model']
            cd.year = self.request.GET['year']
            fmlib.add_car(cd)#to store all info given



       # p.body = fmlib.compile_list() + fmlib.calc_time_span() #to show the given info plus the added utility
       # self.response.write(f.print_out())# print all

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)