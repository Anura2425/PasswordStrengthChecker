# PasswordStrengthChecker
import math

def get_password():
    print("Enter the password you wish to check: ", end="")
    password = input()
    return password

def calculate_entropy(password):
    char_set_size = 0

    # determine size for the character set for the given password
    if any(char.islower() for char in password):
        char_set_size += 26 # lowercase
    if any(char.isupper() for char in password):
        char_set_size += 26 # uppercase
    if any(char.isdigit() for char in password):
        char_set_size += 10 # numbers
    if any(char in "!@#$%^&*()-_=+[]}{|;:'\"\,.<>?/`~" for char in password):
        char_set_size += 32 # special characters

    # in the case that the password entered is empty, return 0
    if char_set_size == 0:
        return 0
    
    # calculate entropy
    entropy = len(password) * math.log2(char_set_size)
    return entropy

def password_strength(entropy):
    if entropy <= 35:
        print("_____________________________________________")
        print("                                             ")
        print("Your password is Very Weak!!! Change it! 😾")
        print("_____________________________________________")
    elif entropy <= 59:
        print("______________________________________________")
        print("                                              ")
        print("Your password is Weak. Could be better... 😿")
        print("______________________________________________")
    elif entropy <= 119:
        print("____________________________________________")
        print("                                            ")
        print("Your password is Strong. Heh... Not bad 😼")
        print("____________________________________________")
    else:
        print("_________________________________________________")
        print("                                                 ")
        print("Your password is Very Stong!!! Holy Moly! 🙀😻")
        print("_________________________________________________")


def main():
    password = get_password()

    entropy = calculate_entropy(password)
    print("Entropy of your password: ")
    print(entropy)
    
    password_strength(entropy)
main()