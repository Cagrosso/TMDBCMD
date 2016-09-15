import tmdbsimple
import textwrap

from utilities import dateParse

from myTypes import TYPE_MOVIE
from myTypes import TYPE_PERSON
from keys import API_KEY

class tmdbObject(object):

    @staticmethod
    def factory(type, query):
        if(type == TYPE_MOVIE):
            return myMovie(query)
        elif(type == TYPE_PERSON):
            return myPerson(query)
        else:
            raise ValueError("Type not recognized, factory failure!")

class myMovie(tmdbObject):

    def __init__(self, query):
        self.myTmdb = tmdbsimple
        self.myTmdb.API_KEY = API_KEY
        self.query = query
        self.search = self.myTmdb.Search()
        self.response = self.search.movie(query = self.query)
        self.topResult = self.response.get('results')[0]
        self.parseDetails()

    def printTopResult(self):
        print(self.topResult)

    def parseDetails(self):
        self.movieTitle = self.topResult.get('title')
        self.releaseDate = self.topResult.get('release_date')
        self.vote_average = str(self.topResult.get('vote_average'))
        self.overview = self.topResult.get('overview')
        self.language = self.topResult.get('language')
        self.genreIDs = ", ".join(str(genre) for genre in self.topResult.get('genre_ids'))
        self.id = str(self.topResult.get('id'))


    def printVerbose(self):
        date = dateParse(self.releaseDate)

        if(self.response == None):
            return ("No Movie found matching that title, try again.")

        outputStr = ""

        if(self.movieTitle != None):
            outputStr += "Movie: " + self.movieTitle
        if(self.releaseDate != None):
            outputStr += "\nRelease Date: " + date
        if(self.genreIDs != None):
            outputStr += "\nGenres: " + self.genreIDs
        if(self.overview != None):
            # use text wrap here to improve readability
            outputStr += "\nSummary: " + self.overview
        if(self.language != None):
            outputStr += "\nLanguage: " + self.language
        if(self.vote_average != None):
            outputStr += "\nAverage User Score: " + self.vote_average

        return outputStr

    def printNormal(self):
        date = dateParse(self.releaseDate)
        outputStr = ""

        if(self.movieTitle != None):
            outputStr += "Movie: " + self.movieTitle
        if(self.releaseDate != None):
            outputStr += "\nRelease Date: " + date
        if(self.overview != None):
            # use text wrap here to improve readability
            outputStr += "\nSummary: " +self.overview

        return outputStr


class myPerson(tmdbObject):

    def __init__(self, query):
        self.myTmdb = tmdbsimple
        self.myTmdb.API_KEY = API_KEY
        self.query = query
        self.search = self.myTmdb.Search()
        self.response = self.search.person(query = self.query)
        self.topResult = self.response.get('results')[0]
        self.parseDetails()

    def printTopResult(self):
        print(self.topResult)

    def parseDetails(self):
        self.name = self.topResult.get('name')
        self.popularity = str(self.topResult.get('popularity'))
        self.knownfor = self.topResult.get('known_for')
        self.id = str(self.topResult.get('id'))

    def printKnownFor(self, verbose):
        movieList = self.knownfor

        output = "\nKnown For: "

        for m in movieList:
            movie = tmdbObject.factory(TYPE_MOVIE, m.get('original_title'))
            title = movie.movieTitle
            summary = movie.overview
            release = movie.releaseDate
            if(verbose):
                # use text wrap to improve readability here
                output += "\n\tTitle: " + title + \
                    "\n\tRelease Date: " + release + \
                    "\n\tSummary: " + summary + "\n"
            else:
                output += title + ", "

        return output

    def printVerbose(self):
        output = ""

        if(self.name != None):
            output += "Name: " + self.name
        if(self.popularity != None):
            output += "\nPopularity: " + self.popularity
        if(self.id != None):
            output += "\nId: " + self.id
        if(self.knownfor != None):
            output += self.printKnownFor(True)

        return output

    def printNormal(self):
        output = ""

        if(self.name != None):
            output += "Name: " + self.name
        if(self.knownfor != None):
            output += self.printKnownFor(False)

        return output
