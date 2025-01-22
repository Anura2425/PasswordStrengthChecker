# PasswordStrengthChecker
import math

def get_password():
    print("Enter the password you wish to check: ", end="")
    password = input()
    return password

def password_to_bits(password):
    encoded_password = password.encode('utf-8') # Encode password to bytes
    return len(encoded_password) * 8 # Multiply by 8 to get number of bits, then return

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
        print("Your password is Very Weak!!! Change it! 😾")
    elif entropy <= 59:
        print("Your password is Weak. Could be better... 😿")
    elif entropy <= 119:
        print("Your password is Strong. Heh... Not bad 😼")
    else:
        print("Your password is Very Stong!!! Holy Moly! 🙀😻")


def main():
    password = get_password()

    bits = password_to_bits(password)
    print(bits)

    entropy = calculate_entropy(password)
    print(entropy)

    password_strength(entropy)
main()