__author__ = 'jacobritenour'


class LanguageGreeting(object):
    def __init__(self):
        self.__greeting = "Hello"

        @property
        def greeting(self):
            return self.__greeting

        @greeting.setter
        def greeting(self,value):
            self.__greeting = value


-----------------------------------------------


lang =LanguageGreeting()
lang.greeting = "Oy!" #uses setter
print lang.greeting   #uses getter

class LanguageGreeting(object):
    def __init__(self):
        self.__greeting = "Hello"

        @property
        def greeting(self):
            return self.__greeting

        @greeting.setter
        def greeting(self,value):
            self.__greeting = value


-------------------------------------------


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #tommy's grades
        t = Transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        print t.final_grade

        #sally's grades
        s = Transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76

class Transcript(object):
    def __init__(self):
        self.grade1 = 0 #no underscores - public
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0 #2 underscores - private

    @property
    def final_grade(self):
        return self.__final_grade





