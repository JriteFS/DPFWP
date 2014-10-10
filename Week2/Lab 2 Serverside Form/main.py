__author__ = 'jacobritenour'

'''
Jacob Ritenour
10/9/2014
DPFWP
Simple Form
'''

import webapp2 #using webapp2 library I could not get the Google app engine to download correctly

class MainHandler(webapp2.RequestHandler): #making a class
    def get(self): #function that is going to make everything work
        page_head = '''
<!DOCTYPE HTML>
<html style="background: tan; max-width: 960px; margin:0 auto;">
    <head>
        <title>Simple Form Assignment</title>
    </head>
    <body>
    <h1 style="background:brown; text:white; text-align:center;">OrderAFish.Org</h1>
    <h3 style="background:brown; text:white; text-align:center;">We have exotic and domestic fishes from around the world!!</h3>
    <h3 style="background:brown; text:white; text-align:center;">Fill out the form below and you too can become the owner of a random fish!!!</h3>
    '''
        page_body = '''<form method="GET">
            <label>Name</label><input type="text" name="username" />
            <label>Email</label><input type="text" name="email" />
            <label>Date of Birth</label><input type="number" name="dob" />
            <label>Street Address</label><input type="text" name="address1" />
            <label>City</label><input type="text" name="city" />
            <label>State</label><select name="state">
                                    <option>Alabama</option>
                                    <option>Florida</option>
                                    <option>Mississippi</option>
                                    <option>Georgia</option>
                                    <option>Texas</option>
                                    <option>Louisana</option>
                                    <option>Tennessee</option>
                                    <option>South Carolina</option>
                                    <option>North Carolina</option>
                                    <option>Arkansas</option>
                                    <option>Oklahoma</option>
                                </select>
            <input type="submit" value="Submit" />'''
        page_end = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            #stores info that came from the form to be used later
            user = self.request.GET['username']
            email = self.request.GET['email']
            dob = self.request.GET['dob']
            address = self.request.GET['address1']
            city = self.request.GET['city']
            state = self.request.GET['state']# i am not sure if this is going to work but i cant really test it due to no google app engine
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


#do not touch
app = webapp2.WSGIApplication([
    ('/',MainHandler)
], debug=True)