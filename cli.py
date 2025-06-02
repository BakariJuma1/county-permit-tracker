from database import session
from models.business import Business
from models.permit import Permit
from models.user import User
from datetime import datetime, timedelta,date
from sqlalchemy import or_,func


def login():
    print("=== Login ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        print(f"Welcome {user.username}! Role: {user.role}")
        return user
    else:
        print("Invalid username or password.")
        return None

def menu(user):
    while True:
        print("\n--- County Permit Tracker ---")
        print("Select an option:")

        # Admin menu
        if user.role == "admin":
            print("1. Register a Business")
            print("2. Issue Permit")
            print("3. Renew Permit")
            print("4. List All Businesses")
            print("5. View Business Permit History")
            print("6. Check Expired Permits")
            print("7. Search Businesses")
            print("8. Logout")

        # Inspector menu
        elif user.role == "inspector":
            print("4. List All Businesses")
            print("5. View Business Permit History")
            print("6. Check Expired Permits")
            print("7. Search Businesses")
            print("8. Logout")

        # Business owner menu
        elif user.role == "owner":
            print("5. View My Business Permit History")
            print("7. Search Businesses")
            print("8. Logout")

        choice = input("Choose an option: ").strip()

        # Admin options
        if user.role == "admin":
            if choice == "1":
                register_business()
            elif choice == "2":
                issue_permit()
            elif choice == "3":
                renew_permit()
            elif choice == "4":
                list_businesses()
            elif choice == "5":
                view_permit_history()
            elif choice == "6":
                check_expired_permits()
            elif choice == "7":
                search_business()
            elif choice == "8":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

        # Inspector options
        elif user.role == "inspector":
            if choice == "4":
                list_businesses()
            elif choice == "5":
                view_permit_history()
            elif choice == "6":
                check_expired_permits()
            elif choice == "7":
                search_business()
            elif choice == "8":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

        # Owner options
        elif user.role == "owner":
            if choice == "5":
                view_permit_history(user)
            elif choice == "7":
                search_business()
            elif choice == "10":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")   

# empty input fields duplicate busines name invalid menu choices
def get_valid_input(prompt, validation_fn, error_msg):
    while True:
        user_input = input(prompt).strip()
        if validation_fn(user_input):
            return user_input
        print(error_msg)

def is_non_empty(s): return len(s) > 0

def register_business():
    print("\n Register new Business")
    name = input("Business Name ")
    owner = input("Owner name ")
    b_type = input("Business Type ")
    location = input("Location ")

    new_business = Business(name=name, owner=owner,business_type=b_type, location=location)
    session.add(new_business)
    session.commit()
    print("Business Registerd Succesfully")

def issue_permit():
    name = input("Enter business name: ").strip()
    fee = float(input("Enter permit fee (KES): "))

    business = session.query(Business).filter_by(name=name).first()
    if not business:
        print("Business not found.")
        return

    issue_date = datetime.now()
    expiry_date = issue_date + timedelta(days=365)

    permit = Permit(
        fee=fee,
        issue_date=issue_date,
        expiry_date=expiry_date,
        business=business
    )

    session.add(permit)
    session.commit()
    print(f"Permit issued to {business.name} successfully.")
       
def renew_permit():
    print("\n Renew Permit")
    permit_number = input("Enter Permit Number to Renew: ").strip()
    permit = session.query(Permit).filter_by(permit_number=permit_number).first()

    if not permit:
        print("Permit Not Found.")
        return

    permit.issue_date = date.today()
    permit.expiry_date = permit.issue_date + timedelta(days=90)
    session.commit()
    print("Permit Renewed Successfully")


def list_businesses():
    print("\n Registerd  Businesses")
    businesses = session.query(Business).all()
    for biz in businesses:
        print(f"ID:{biz.id},Name:{biz.name},Owner:{biz.owner},Type:{biz.business_type},Location:{biz.location}")

def view_permit_history():
    print("\n Permit History")
    business_id = int(input("Enter Business ID: "))
    business = session.query(Business).get(business_id)

    if business:
        for permit in business.permits:
            status = "Expired" if permit.is_expired else "Active"
            print(f"{permit.permit_number} | Issued: {permit.issue_date} | Expires: {permit.expiry_date} | Status: {status}")
    else:
        print("Business not found.")

def check_expired_permits():
    print("\n Expired Permits:")
    permits = session.query(Permit).all()
    for permit in permits:
        if permit.is_expired:
            print(f"{permit.permit_number} (Business ID: {permit.business_id}) expired on {permit.expiry_date}")  

def search_business():
    term = input("Enter name or location to search: ").lower()
    results = session.query(Business).filter(
        or_(
            Business.name.ilike(f"%{term}%"),
            Business.location.ilike(f"%{term}%")
        )
    ).all()
    for b in results:
        print(f"{b.name} - {b.location}")

def view_total_revenue():
    total = session.query(Permit).with_entities(func.sum(Permit.fee)).scalar()
    print(f"Total Revenue from Permits: KES {total if total else 0}")

