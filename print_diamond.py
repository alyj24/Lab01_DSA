def print_header(text, color_code):
    print(f"\033[{color_code}m" + "=" * 42)
    print(text.center(42, "="))
    print("=" * 42)

print_header("Laboratory Activity 01 ~ Python Review", 96)