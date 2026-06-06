# Write a program that:
# 1. Asks user to enter a number
# 2. Divides 100 by that number
# 3. If user enters 0 → print "Cannot divide by zero!"
# 4. If user enters text → print "Please enter a number!"
# 5. Finally → print "Program finished!"

try:
    user = int(input("Enter a number = "))
    result = 100 // user
    print(f"Result:{result}")
except ZeroDivisionError:
    print("cannot divide by zero!") 
except ValueError:
    print("Please enter a number!") 
finally:
    print("Program finished")       


# Create a function safe_divide(a, b)
# 1. Try to divide a by b
# 2. If b is zero → return "Cannot divide by zero!"
# 3. If wrong type → return "Invalid input!"
# 4. Else → return the result

def safe_divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input"
    
print(safe_divide(100,5))
print(safe_divide(100,0))
print(safe_divide(100,"abc"))


# Create a function open_file(filename)
# 1. Try to open the file
# 2. If file not found → print "File not found!"
# 3. Finally → print "Done!"
        

def open_file(filename):
    try:
        file = open(filename,"r")
        print("File open successfuly")
    except FileNotFoundError:
        print ("File not found error")
    finally:
        print("Done")

open_file("text.txt")



# As usual problem solve to open the file.


def open_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Done!")


open_file("test.txt")