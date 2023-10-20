def divide_numbers():
    try:
        x = int(input("Enter a: "))
        y = int(input("Enter b: "))
        result = x/y
        print('result=', result)
    except ValueError:
        print("invalid input. please try again")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print("An error occurred: ", str(e))

divide_numbers()