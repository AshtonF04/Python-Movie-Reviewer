def main():
    print("--------------------")
    print("     WELCOME TO     ")
    print("PYTHON MOVIE REVIEWER")    
    print("--------------------")

    running = True
    while running:
        try:
            # Output user options
            print("What would you like to do?")
            print("  1. View Reviews")
            print("  2. Add new review")
            
            # Check choice and run appropriate code
            choice = int(input())
            match choice:
                case 1:
                    print("Listing all movies...")
                case 2:
                    print("Adding a new movie...")
                case _:
                    print("Invalid Choice")
                    continue
            
        except ValueError:
            print("Invalid Choice.")
            continue

if __name__ == "__main__":
    main()