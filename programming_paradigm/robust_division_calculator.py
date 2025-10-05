def safe_divide(numerator, denominator):
    try:
        result = (float(numerator))/(float(denominator))
        return print(f"The result of the division is {result}")
    


    except ZeroDivisionError:
        return print(" Error: Cannot divide by zero.")

    except ValueError:
        return print("Error: Please enter numeric values only.")
