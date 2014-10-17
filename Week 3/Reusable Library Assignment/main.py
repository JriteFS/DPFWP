__author__ = 'jacobritenour'

'''
Jacob Ritenour
10-16-2014
DPFWP
Reusable Library Assignment
'''
import webapp2
from lib import CarData, FavoriteCars
from page import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for form
        f = FormPage()


class FormPage(object):
    def get(self): #function that is going to make everything work

        fmlib = FavoriteCars()
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
    </body>
</html>'''
        if self.request.GET:
            #stores info that came from the form to be used later
            make = self.request.GET['make']#add this to the array
            model = self.request.GET['model']
            year = self.request.GET['year']
            fmlib.add_car(make,model,year)



        #page for class
        p = ResultsPage()

        p.body = fmlib.compile_list() + fmlib.calc_time_span()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)