__author__ = 'jacobritenour'

#I attempted to add the form to this page but i do not know how to call it and generate it. Please advise so i can correct my code.


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