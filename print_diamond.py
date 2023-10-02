def print_header(text, color_code):
    print(f"\033[{color_code}m" + "=" * 42)
    print(text.center(42, "="))
    print("=" * 42)
# write a python function named print_diamond that takes an odd integer n as an argument
# and prints a diamond shape with a width of n using the * character.

# pseudocode
# establish the function
def print_diamond(n, color_code):

    for i in range(1, n + 1, 2):
        alignment = " " * ((n - i) // 2)
        character = "*" * i
        print(f"\033[{color_code}m{alignment}{character}{alignment}")

    for i in range(n - 2, 0, -2):
        alignment = " " * ((n - i) // 2)
        character = "*" * i
        print(f"\033[{color_code}m{alignment}{character}{alignment}")

    if n % 2 == 0:
        print(f"\033[94mPlease provide an odd integer.")
        return

# run the program
argu_n = 5
print_diamond(argu_n, 95)

# end
