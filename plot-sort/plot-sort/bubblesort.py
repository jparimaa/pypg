def sort(input):
    for i in range(len(input) - 1, 0, -1):
        for j in range(i):
            if input[j] > input[j + 1]:
                temp = input[j]
                input[j], input[j + 1] = input[j + 1], input[j]