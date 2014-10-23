__author__ = 'jacobritenour'

'''
Jacob Ritenour
10-16-2014
DPFWP
Reusable Library Assignment
'''
import webapp2 #how do I get this?
from lib import CarData, FavoriteCars # importing from the other 2 py pages
from page import ResultsPage #importing to report the resultes

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for form
        f = FormPage()

#I am not sure this will work correctly please advise on how  i can correct it.
class FormPage(object):
    def get(self): #attempting this function that is going to make everything work

        fmlib = FavoriteCars()

        #form to collect make, model, amd year of vehicle
        form_top = '''
<!DOCTYPE HTML>
<html style="background: tan; max-width: 960px; margin:0 auto;">
    <head>
        <title>Favorite vehicle</title>
    </head>
    <body>
    <h1 style="text-align:center;">Enter Your Favorite Vehicle</h1>
    <h3 style="text-align:right;">Create a DataBase of your favorite vehicles here!!</h3>
    <h3 style="text-align:center;">Fill out the form below and begin today!!!</h3>
    '''
        form_mid = '''<form method="GET">
            <label>make</label><input type="text" name="make" />
            <label>Model</label><input type="text" name="model" />
            <label>Year</label><input type="number" name="year" />
            <input type="submit" value="Submit" />'''
        form_end = '''
        </form>
        <footer>If you wish to continue to save your list make sure you save the link above.</footer>
    </body>
</html>'''
        cd = CarData()#calling car data info
        if self.request.GET:
            #stores info that came from the form to be used later
            cd.make = self.request.GET['make']#add this to the array
            cd.model = self.request.GET['model']
            cd.year = self.request.GET['year']
            fmlib.add_car(cd.make,cd.model,cd.year)#to store all info given



        #page for class
        p = ResultsPage()

        p.body = fmlib.compile_list() + fmlib.calc_time_span() #to show the given info plus the added utility
        self.response.write(p.print_out())# print all

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)