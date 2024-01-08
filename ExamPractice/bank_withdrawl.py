def get_total_amount(a: int, b: int, c: int) -> int:
    sum = 100*a + 500*b + 1000*c
    return sum

num_hundred = int(input("How many 100 notes: "))
num_five_hundred = int(input("How many 500 notes: "))
num_thousand = int(input("How many 1000 notes: "))

total_amount = get_total_amount(num_hundred, num_five_hundred, num_thousand)
print(f"Total amount withdrawn: {total_amount}")
