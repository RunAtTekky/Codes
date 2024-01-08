n = int(input())

print(f"Binary representation of number before shifting: ")
print(bin(n)[2::])

n = n<<4

print(f"Binary representation of number after shifting: ")
print(bin(n)[2::])

