f = open("salary.txt", "w")

f.write("10000")
f.write("\n")
f.write("10003")
f.write("\n")
f.write("12000")
f.write("\n")
f.write("15003")
f.write("\n")
f.write("20000")
f.write("\n")
f.write("50003")

f.close()


f = open("salary.txt", "r")

sum = 0
while True:
    l = f.readline()
    if (l == ''):
        break
    sum += int(l)
    print(l)

print("\n")
print(f"Sum is {sum}")
