from cli import menu
from database import session

if __name__== "__main__":
    try:
       menu()
    except KeyboardInterrupt:
        print("\n Operation cancelled by User")   
    finally:
        session.close()    