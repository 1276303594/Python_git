for i in range(100, 1000):
    first_number, second_number, third_number = map(int, str(i))
    if i == (
            first_number**3
            + second_number**3
            + third_number**3):
        print(i)
