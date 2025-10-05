def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        return result
    


    except ZeroDivisionError:
        print("Cannot divide by Zero ")

    except ValueError:
        print("Error: Please enter numeric values only.")

