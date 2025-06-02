from cli import menu, login
from database import session

def main():
    user = None
    while not user:
        user = login()
    
    menu(user)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    finally:
        session.close()
