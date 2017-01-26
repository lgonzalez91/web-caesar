def encrypt(text,rot):
    rotated_text = ""
    for letter in list(text):
        rotated_text = rotated_text + rotate_character(letter,rot)
    return rotated_text

def user_input_is_valid(cl_args):
    if len(cl_args) == 1:
        return False
    if cl_args[1].isdigit() == False:
        return False
    return True

import string
def alphabet_position(char):
    lower_case_alphabet = list(string.ascii_lowercase)
    upper_case_alphabet = list(string.ascii_uppercase)
    if char in lower_case_alphabet:
        return lower_case_alphabet.index(char)
    if char in upper_case_alphabet:
        return upper_case_alphabet.index(char)

def rotate_character(char,rot):
    lower_case_alphabet = string.ascii_lowercase
    upper_case_alphabet = string.ascii_uppercase
    if char not in lower_case_alphabet and char not in upper_case_alphabet:
        return char
    if char in lower_case_alphabet:
        rotated_char = lower_case_alphabet[(alphabet_position(char) + rot)%26]
    if char in upper_case_alphabet:
        rotated_char = upper_case_alphabet[(alphabet_position(char) + rot)%26]
    return rotated_char
