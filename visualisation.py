import time
def calc_square(numbers):
    for n in numbers:
        print(f"\n{n}^2 = {n&n}")
        time.sleep(0.1)

def calc_cube(numbers):
    for n in numbers:
        print(f"\n{n}^3 = {n*n*n}")
        time.sleep(0.1)

numbers = [int(x) for x in range(1,11)]
start = time.time()
# calc_square(numbers)
calc_cube(numbers)
end = time.time()

print("Execution time: {}".format(end-start))