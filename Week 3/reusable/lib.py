__author__ = 'jacobritenour'


class FavoriteCars(object):
    def __init__(self):
        self.__car_list = []

    def add_car(self, m):
        self.__car_list.append(m)
        print self.__car_list

    def compile_list(self):
        output = ''
        for car in self.__car_list: #for each of the cars added
            output += 'Make: ' + car.make + ' (' + str(car.year) + ') Model: ' + car.model +' <br />'
        return output


    def calc_time_span(self):
        '''
        calculate the years between cars
        '''
        #years
        years = []
        for car in self.__car_list:
            years.append(car.year)

        #sort years from High to Low
        years.sort()

        #subtract the low years from the high year
        num = len(years) - 1 #oldest year
        #span = years[num] - years[0] #highest years - lowest years
        return 'The number of years between the oldest and newest cars is ' + str(3)
        #return the span of time
    #have an array to hold the movie info
    #some way to add to that array
    #some way to generate a list of all movies
    #calculate time span between movies

    @property
    def car_list(self):
        return self.__car_list


class CarData(object): #data Object
    def __init__(self):
        self.make = ''
        self.__year = 0 #check for valid year
        self.model = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2015:
            print "Error, Invalid Year!!!" #going to give an error if over 2014
            self.__year = 2015
        else:
            self.__year = y #will apply the date given