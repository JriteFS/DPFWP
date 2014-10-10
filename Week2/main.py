__author__ = 'jacobritenour'

import webapp2 #using webapp2 library

class MainHandler(webapp2.RequestHandler): #making a class
    def get(self): #function that is going to make everything work
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET">
            <label>Name</label><input type="text" name="username" />
            <label>Email</label><input type="text" name="email" />
            <label>Date of Birth</label><input type="text" name="dob" />
            <label>Email</label><input type="text" name="email" />
            <input type="submit" value="Submit" />'''
        page_end = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            #stores info that came from the form to be used later
            user =  self.request.GET['username']
            email =  self.request.GET['email']
            dob =  self.request.GET['dob']
            self.response.write(page_head + user + '' + email + page_body + page_end)
        else:
            self.response.write(page_head + page_body + page_end) #Printing the info


#do not touch
app = webapp2.WSGIApplication([
    ('/',MainHandler)
], debug=True)