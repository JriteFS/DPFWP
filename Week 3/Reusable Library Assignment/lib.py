__author__ = 'jacobritenour'


class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

    def add_movie(self, m):
        self.__movie_list.append(m)

    def compile_list(self):
        output = ''
        for movie in self.__movie_list: #for each of the movies added
            output += 'Title: ' + movie.title + ' (' + str(movie.year) + ') Directed By: ' + movie.director +' <br />'
        return output


    def calc_time_span(self):
        '''
        calculate the time between movies
        '''
        #years
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        #sort years from High to Low
        years.sort()

        #subtract the low years from the high year
        num = len(years) - 1 #oldest year
        span = years[num] - years[0] #highest years - lowest years
        return 'The number of between the oldest and newest movie is ' + str(span)
        #return the span of time
    #have an array to hold the movie info
    #some way to add to that array
    #some way to generate a list of all movies
    #calculate time span between movies

    @property
    def movie_list(self):
        return self.__movie_list


class MovieData(object): #data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2014:
            print "Error, Invalid Year!!!" #going to give an error if over 2014
            self.__year = 2014
        else:
            self.__year = y #will apply the date given