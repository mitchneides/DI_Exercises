
def binary_to_dec(binary):
    bin = binary
    total = 0
    counter = 0
    while bin != 0:
        rem = bin % 10
        total = total + (rem * (2 ** counter))
        counter += 1
        bin = bin//10

    print(total)
    return total


binary_to_dec(1010100100)


def dec_to_binary(decimal):
    dec = decimal
    list = []
    while dec != 0:
        rem = dec % 2
        list.append(rem)
        dec = dec // 2

    reverse = list[::-1]
    answer = ''
    for every in reverse:
        answer = answer + str(every)

    print(answer)
    return answer


dec_to_binary(9)