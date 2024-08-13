import random

def get_passwd_length():
    entry = input("Enter the password length: ")
    try:
        length = int(entry)
        if length <= 0:
            raise ValueError
        return length
    except ValueError:
        print("ERROR: The length must be a positif integer !!!")

def generete_passwd(length):
    passwd = ''
    for i in range(length):
        passwd += chr(random.randint(33, 126))
    return passwd


def main():
    # Getting the password length
    length = get_passwd_length()
    # Generete the password
    print(f"\nPassword: {generete_passwd(length)}\n")
    # Loop
    while True:
        entry = input("Do you want to quit(yes/no) ").lower()
        if entry == "yes":
            print("GoodBye :)")
            break
        elif entry == "no":
            # Getting the password length
            length = get_passwd_length()
            # Generete the password
            print(f"\nPassword: {generete_passwd(length)}\n")
        else:
            print("Entry Error, please enter yes/no")

if __name__ == "__main__":
    main()