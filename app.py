file = open('file.txt', 'r')
file_content = file.read()

file.close()

print(file_content)



user_name = input("Enter username: ")
file_writing = open('file.txt', 'w')

file_writing.write(user_name)

file_writing.close()