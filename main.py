from cli import menu, login, register_user
from database import session

def main():
    user = None
    while not user:
        print("\nWelcome to County Permit Tracker")
        print("1. Login")
        print("2. Register")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "1":
            user = login()
        elif choice == "2":
            register_user()
        else:
            print("Invalid choice. Please try again.")

    menu(user)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    finally:
        session.close()
