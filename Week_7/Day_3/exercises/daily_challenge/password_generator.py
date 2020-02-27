import random
import string


def get_pw_length():
    pw_len = input("How many characters would you like to be in your password? \n(Must be between 6 and 30 characters) \nEnter your response: ")
    return int(pw_len) if 6<=int(pw_len)<=30 else print('Invalid Input. Goodbye.')


def generate_pw(pwLength):
    pw = []
    acceptable = list(string.printable)

    pw.append(acceptable[random.randint(0,9)])
    pw.append(acceptable[random.randint(10,35)])
    pw.append(acceptable[random.randint(36,61)])
    pw.append(acceptable[random.randint(62,84)])

    while len(pw)<pwLength:
        pw.append(acceptable[random.randint(0,84)])

    random.shuffle(pw)
    print("Your new password: "+''.join(pw))
    return ''.join(pw)


if __name__ == '__main__':
    l = get_pw_length()
    generate_pw(l)