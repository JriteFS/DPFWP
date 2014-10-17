__author__ = 'jacobritenour'

class FormPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css.styles.css"
        self.__head = ""
     page_head = '''
<!DOCTYPE HTML>
<html style="background: tan; max-width: 960px; margin:0 auto;">
    <head>
        <title>Add Your Favoite Vehicles</title>
    </head>
    <body>
    '''
        page_body = '''<form method="GET">
            <label>Make</label><input type="text" name="make" />
            <label>Model</label><input type="text" name="model" />
            <label>Year</label><input type="number" name="year" />
            <label>Street Address</label><input type="text" name="address1" />
            <label>City</label><input type="text" name="city" />
            <label>State</label>
            <input type="submit" value="Submit" />'''
        page_end = '''
        </form>
</html>'''
        if self.request.GET:
            #stores info that came from the form to be used later
            make = self.request.GET['make']
            model = self.request.GET['model']
            year = self.request.GET['year']


            self.response.write(page_head #listing everything i want to show
                                + user + ''
                                + email + ''
                                + dob + ''
                                + address + ''
                                + city + ''
                                + state + ''#i am hoping this select drop down works
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