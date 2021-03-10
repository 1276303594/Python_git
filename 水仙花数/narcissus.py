for i in range(100, 10000):
    index = len(str(i))
    if i < 1000:
        first_number, second_number, third_number = map(int, str(i))
        if (i == (
                first_number**index
                + second_number**index
                + third_number**index)):
            print(i, end=',')
    elif (999 < i < 10000):
        first_number, second_number, third_number, fourth_number = map(int, str(i))
        if (i == (
                first_number**index
                + second_number**index
                + third_number**index
                + fourth_number**index)):
            print(i, end=',')
