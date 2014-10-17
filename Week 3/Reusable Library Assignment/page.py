__author__ = 'jacobritenour'


class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css.styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
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