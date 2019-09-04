file = open('file.txt', 'r')
file_content = file.read()
file.close()
print(file_content)


user_name = input("Enter username: ")
my_file_writing= open('file.txt', 'w')

my_file_writing.write(user_name)

my_file_writing.close()

