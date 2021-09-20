import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("ASK_love_sandwiches")


def get_sales_data():
    """
    Get Sales Data
    """
    while True:
        print("Please enter sales data from the last market")
        print("Data should be  sic numbers, separated by coma")
        print("Example:10,20,30,40,50,60\n")

        data_str = input("enter your data here: ")

        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("Data is valid")
            break
        return sales_data


def validate_data(values):
    """
    converts data into integers, gives Error if number of values is not 6
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 numbers is required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again\n")
        return False
    
    return True

    
data = get_sales_data()