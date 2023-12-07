'''
opens in write mode
f = open("python.txt","w") 
writes the data in the file
f.write("Monty Python's Fliynig Circus")
closes the file object
f.close()
'''

# 1st example
# f = open("python.txt","w")
# f.write("Monty Python's Flying Circus")
# f.close()

# 2nd example
lines = ["Beautiful is better than ugly \n",
         "Explicit is better than implicit \n",
         "Simple is better than complex",
         "Complex is better bruh than complicated"]

f = open("pythonLines.txt","w")
f.writelines(lines)
f.close()

f = open("pythonLines.txt",'r')
print()
print(f.readlines())
# while True:
#     line = f.readline()
#     if line == '':
#         break
#     print(line)
# print()
f.close()
