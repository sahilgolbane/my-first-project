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