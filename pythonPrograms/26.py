# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix():
    string = input("Enter the string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")

    if string.startswith(prefix):
        print(f"The string starts with the prefix '{prefix}'.")
    else:
        print(f"The string does not start with the prefix '{prefix}'.")

    if string.endswith(suffix):
        print(f"The string ends with the suffix '{suffix}'.")
    else:
        print(f"The string does not end with the suffix '{suffix}'.")


check_prefix_suffix()
