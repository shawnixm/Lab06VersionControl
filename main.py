# Shawnick Wang
def encode(password):
    encoded_password = ""
    for num in password:
        if int(num) < 7:
            encoded_num = int(num) + 3
        else:
            encoded_num = (int(num) + 3) % 10
        encoded_password += str(encoded_num)
    return encoded_password

if __name__ == "__main__":
    password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        user_selection = int(input("Please enter an option: "))
        if user_selection == 1:
            user_password = input("Please enter your password to encode: ")
            password = encode(user_password)
            print("Your password has been encoded and stored!")
            print()
        if user_selection == 2:
            print(f"The encoded password is {password}, and the original password is .\n")
        if user_selection == 3:
            break