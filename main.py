import argparse
import TMDBHandler

from myTypes import TYPE_MOVIE as MOVIE
from myTypes import TYPE_PERSON as PERSON

def main():
    descStr = "A program that outputs imformation from The Movie Database"

    parser = argparse.ArgumentParser(
        description=descStr
    )

    """
    Get information on a single movie
    """

    parser.add_argument(
        "--movie",
        dest='movieTitle',
        help="Enter a movie title in double-quotes to receive information on the best match movie"
    )

    """
    Get information on a single person
    """
    parser.add_argument(
        "--person",
        dest='personName',
        help="Enter an Actor or Actress' name in double-quotes to receive information on the best match person"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action='store_true',
        help="Enable verbose output on the option selected"
    )

    args = parser.parse_args()

    if args.movieTitle:
        movie = TMDBHandler.tmdbObject.factory(MOVIE, args.movieTitle)
        if args.verbose:
            print(movie.printVerbose())
        else:
            print(movie.printNormal())



    if args.personName:
        person = TMDBHandler.tmdbObject.factory(PERSON, args.personName)
        if args.verbose:
            print(person.printVerbose())
        else:
            print(person.printNormal())


if __name__ == "__main__":
    main()