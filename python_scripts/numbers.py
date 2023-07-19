def get_numbers(n):
    even_numbers = []
    odd_numbers = []
    for i in range (1, n+1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return even_numbers, odd_numbers


n = 50


even_number, odd_numbers = get_numbers(n)
print("print even numbers upto 50:, ", even_number)
print("print odd number upto 50:, ", odd_numbers)