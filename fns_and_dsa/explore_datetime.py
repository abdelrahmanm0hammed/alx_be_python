from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():

    
    print(f"Current date and time : {current_date}")
def calculate_future_date():
   
    num_of_days = int(input("Enter the number of days to add to the current date: "))
   
    Future_date = timedelta(days=num_of_days) + current_date

    print(f"Future date: {Future_date}")

display_current_datetime()
calculate_future_date()
