from Movie import Movie

def add_review():
    try:
        print()
        print("--------------")
        print("Add Movie Menu")
        print("--------------")
        title = input("Enter the movie title: ")
        release_year = int(input("Enter the release year: "))
        genre = input("Enter the movie genre: ")
        rating = int(input("Rate the movie 1-10⭐️: "))

        Movie.add_review(title, release_year, genre, rating)
    except ValueError:
        print("***Invalid entry, returning to menu...***")
        return

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
            
            # Check choice and run appropriate code
            print()
            choice = int(input("Selection: "))
            match choice:
                case 1:
                    print("Listing all movies...")
                case 2:
                    add_review()
                case _:
                    print("***Invalid Choice***")
                    continue
            
        except ValueError:
            print("***Invalid Choice.***")
            continue

if __name__ == "__main__":
    main()