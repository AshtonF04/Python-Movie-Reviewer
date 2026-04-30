import json

from Movie import Movie
from SaveUtil import SaveUtil

def add_review():
    try:
        # Get movie information from user
        print()
        print("--------------")
        print("Add Movie Menu")
        print("--------------")
        title = input("Enter the movie title: ")
        release_year = int(input("Enter the release year: "))
        genre = input("Enter the movie genre: ")
        rating = int(input("Rate the movie 1-10⭐️: "))

        # Add movie to database and print confirmation message
        movie = Movie.add_review(title, release_year, genre, rating)
        str_len = len(str(movie))
        print("-" * (str_len + 40))
        print(f"{movie} was successfully added to the database.")
        print("-" * (str_len + 40))
    except ValueError:
        print("***Invalid entry, returning to menu...***")
        return
    
def list_reviews():
    print()
    print("------------")
    print("Your Reviews")
    print("------------")

    Movie.list_reviews()

def save_reviews():
    print("---------")
    print("Saving...")
    print("---------")

    reviews = SaveUtil.toDict(Movie.reviews)
    with open("save.json", "w") as f:
        json.dump(reviews, f, indent=4)



def main():
    print("--------------------")
    print("     WELCOME TO     ")
    print("PYTHON MOVIE REVIEWER")    
    print("--------------------")

    running = True
    while running:
        try:
            # Output user options
            print()
            print("What would you like to do?")
            print("  1. View Reviews")
            print("  2. Add new review")
            print("  3. Save")
            print("  4. Exit")
            
            # Check choice and run appropriate code
            print()
            choice = int(input("Selection: "))
            match choice:
                case 1:
                    list_reviews()
                case 2:
                    add_review()
                case 3:
                    save_reviews()
                case 4:
                    print("Exiting...")
                    running = False
                case _:
                    print("***Invalid Choice***")
                    continue
            
        except ValueError:
            print("***Invalid Choice.***")
            continue

if __name__ == "__main__":
    main()