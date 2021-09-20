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
    print("Please enter sales data from the last market")
    print("Data should be  sic numbers, separated by coma")
    print("Example:10,20,30,40,50,60\n")

    data_str = input("enter your data here: ")
    print(f"the data entered is: {data_str}")

get_sales_data()
