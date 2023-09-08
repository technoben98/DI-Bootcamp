while True:
    input_number = int(input("Type your positive number:\n"))
    if input_number == 0:
        break

    sum_of_dividers = 0

    for i in range(1, input_number):
        if  input_number % i == 0:
            sum_of_dividers = sum_of_dividers + i

    if (sum_of_dividers == input_number):
        print(f"Number {input_number} is a perfect number.")
    else:
        print(f"Number {input_number} is not a perfect number.")