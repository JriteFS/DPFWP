__author__ = 'jacobritenour'


from lib import FavoriteCars, CarData
#I attempted to add the form to this page but i do not know how to call it and generate it. Please advise so i can correct my code.

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

    def print_out(self):
        all = self.make + " " + self.model + " " + self.year
        return all#should show everything listed one after the other.

class ResultsPage(object):#produce the results pages
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css.styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Please enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = ""
        self.__error = ''
        self.__close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all#should show everything listed one after the other.