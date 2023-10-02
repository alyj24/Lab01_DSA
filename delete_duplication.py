def print_header(text, color_code):
    print(f"\033[{color_code}m" + "=" * 42)
    print(text.center(42, "="))
    print("=" * 42)

# create a program that will delete all duplicate characters in a string
# pseudocode
while True:
      # define the string
      input_str = input("\033[91mGood Day! Please enter the given string or 'charl' if it is done: ")

      # to enter a new string or end the program
      if input_str.lower() == 'charl':
          break

      # initiate an empty string to store and delete duplication of characters
      delete = ""
      # establish the function
      for char in input_str:
          char_lower = char.lower()
          if input_str.lower().count(char_lower) == 1:
              delete += char
      result = delete.replace(" ", "")

      # run the program
      print("\033[94m" + result)

      # to end the loop
      print("\033[92mYahoo!")
      print_header("Laboratory Activity 01 ~ Python Review", 96)

