# To write contents in the file
salary = open("salary.txt", 'w')

salary.writelines("10000\n")
salary.writelines("2000\n")
salary.writelines("1200\n")
salary.writelines("13400\n")
salary.writelines("21000\n")

salary.close()

# Read contents from file
salary = open("salary.txt",'r')

while True:
    f = salary.readline()
    if f == '':
        break
    print(f)

salary.close()
