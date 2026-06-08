# 1. Create a file called "notes.txt"
# 2. Write these 3 lines:
#    - "My name is Sahil"
#    - "I am learning Python"
#    - "I will get a job soon!"
# 3. Then read and print the file

try:
    file = open("notes.txt","w")
    file.write("My name is sahil\n")  
    file.write("I am learning python\n")
    file.write("I will get a job soon!\n")
    file.close()
    print("File written successfully")
except:
    print("Something went wrong")   

finally:
    print("Done")

file = open("notes.txt","r")
print(file.read())
file.close()

# Apennding!


try:
    file = open("notes.txt","a")
    file.write("This is line 4\n")
    file.write("This is line 5\n")
    file.close()
    print("File done successfully")
except:  
    print("Something went wrong") 
finally:
    print("Done!")

file = open("notes.txt","r")
print(file.read())
file.close()