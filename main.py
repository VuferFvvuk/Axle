from tkwindow import StartWindows

if __name__ == "__main__":
    production = 1
    x = 4
    for degree in range(1, 7):
        if x != 2 ** degree:
            production *= (x - (2 ** degree - 1)) / (x - (2 ** degree))
        print(2 ** degree)

    print(production)

    # productio = 1
    # x = 5
    # for degree in range(1, 65):
    #     productio *= (x - (degree - 1)) / (x - degree)
    #     # print(2 **degree)
    #
    # print(productio)