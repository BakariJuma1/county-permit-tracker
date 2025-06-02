from database import session
from models.business import Business
from models.permit import Permit
from datetime import date, timedelta


def menu():
    while True:
        print("\n County Permit Tracker")
        print("1. Register a Business ")
        print("2. Issue Permit") 
        print("3. Renew Permit ")
        print("4. List All Businesses") 
        print("5. View Business Permit History") 
        print("6. Check Expired Permits")
        print("7. Exit") 

        choice= input('Choose an option')

        if choice =='1':
            register_business()
        elif choice =="2":
            issue_permit()
        elif choice =="3":
            renew_permit()
        elif choice =="4":
            list_businesses()
        elif choice == "5":
            view_permit_history()
        elif choice == "6":
            check_expired_permits()
        elif choice == "7":
            print("Goodbye")
            break
        else:
            print("Invalid choice")            
def register_business():
    print("\n Register new Business")
    name = input("Business Name")
    owner = input("Owner name")
    b_type = input("Business Type")
    location = input("Location")

    new_business = Business(name=name, owner=owner,business_type=b_type, location=location)
    session.add(new_business)
    session.commit()
    print("Business Registerd Succesfully")

def issue_permit():
    print("\n Register new Business")
    business_id = int(input("Enter Business Id:"))  
    permit_number = input("Permit Number")
    issue = date.today()
    expiry = issue + timedelta(days=90)

    new_permit = Permit(permit_number=permit_number,issue_date=issue, expiry_date=expiry)
    session.add(new_permit)
    session.commit()
    print("Permit Issued Succesfully")  

       
def renew_permit():
    print("\n Renew Permit")
    permit_number = input("Enter Permit Number to Renew")
    permit = session.query(Permit).filter_by(permit_number=permit_number).first()

    if permit:
        permit.issue_date = date.today()
        permit.expiry_date = permit.issue_date + timedelta(days=90)
        session.commit()
        print("Permit Renewed")
    else:
        print("Permit Not Found")

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


        