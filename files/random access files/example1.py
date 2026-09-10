try:
    with open('files/file.txt', 'r') as file:
        print('Initially file pointer position:', file.tell()) #0
        file.seek(5)
        print('File pointer position after seek:', file.tell()) #5
        print('Content from current position:', file.read())
        print('File pointer position after read:', file.tell()) #end of file
except FileNotFoundError:
    print('File not found. Please check the file path.')