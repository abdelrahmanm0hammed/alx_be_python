from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():

    
    print(f"Current date and time : {current_date}")
def calculate_future_date():
   
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(num_of_days)
    Future_date = duration + current_date

    print(f"Future date: {Future_date}")

display_current_datetime()
calculate_future_date()