import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = "b0jAddiWaMf_3scH2wPKs4xfUXnPcDyfL7PPiTvznS5F"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_expense")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    print("Inserting data:")
    print("Period:", period)
    print("Incomes:", incomes)
    print("Expenses:", expenses)
    print("Comment:", comment)
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})

def update_period(period, new_incomes, new_expenses, new_comment):
    """Updates an existing record with new data"""
    existing_data = db.get(period)
    if existing_data:
        existing_data["incomes"] = new_incomes
        existing_data["expenses"] = new_expenses
        existing_data["comment"] = new_comment
        db.put(existing_data)
        return True
    else:
        st.error(f"Period {period} not found for update.")
        return False
        
def delete_period(period):
    """Deletes a record for a given period"""
    existing_data = db.get(period)
    if existing_data:
        db.delete(existing_data.key)
        return True
    else:
        st.error(f"Period {period} not found for delete.")
        return False

def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
