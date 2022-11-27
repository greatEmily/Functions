user_text = input("Enter text: ")

user_choice = input("Enter 1 for uppercase and 2 for lowercase: ")

if user_choice == "1":
  print(user_text.upper())
elif user_choice == "2":
  print(user_text.lower())
else:
  print("Choice not valid. Please try again.")