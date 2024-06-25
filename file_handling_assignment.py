def create_and_write_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("12345 is a number.\n")
            file.write("This is the third line.\n")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation and writing completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading completed.")

def append_to_file():
    try:       
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("67890 is another number.\n")
            file.write("This is the last appended line.\n")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending completed.")

if __name__ == "__main__":
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()