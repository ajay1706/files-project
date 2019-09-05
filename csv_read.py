file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()


lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data= line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].upper()
    degree = person_data[3]


    print(f'{name} is {age}, studying {degree} at {university}')


sample_csv_value = ','.join(['Rolf','23','IIT','Computing'])
print(sample_csv_value)
#writing into csv file











