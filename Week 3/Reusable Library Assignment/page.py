__author__ = 'jacobritenour'

class FormPage(object):
    def get(self): #function that is going to make everything work
        page_head = '''
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
        page_body = '''<form method="GET">
            <label>make</label><input type="text" name="make" />
            <label>Model</label><input type="text" name="model" />
            <label>Year</label><input type="number" name="year" />
            <input type="submit" value="Submit" />'''
        page_end = '''
        </form>
        <p style="background:brown; text:white; text-align:center;">We hope you enjoy your Fish!!</p>
        <footer style="background:brown; text:white;">Be Aware that one of our personnel when be sending you an email to verify the available living space and your ability to care for this animal. They may also make a home visit just to ensure the safety of all wildlife handled by our organization. If you refuse to allow our personnel we can/will deny you from being the proud parent of an amazing creature of the sea.</footer>
    </body>
</html>'''
        if self.request.GET:
            #stores info that came from the form to be used later
            make = self.request.GET['make']#add this to the array
            model = self.request.GET['model']
            year = self.request.GET['year']

            self.response.write(page_head #listing everything i want to show
                                + make + ''
                                + model + ''
                                + year + ''
                                + page_end) #this will display the info placed in but not the body
        else:
            self.response.write(page_head + page_body + page_end) #Printing the info this will display every as normal



class ResultsPage(object):
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
        return all