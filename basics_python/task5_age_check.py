age = int(input("Enter age: "))

if age >= 0 and age < 18:
    print("you're a child")
elif age >= 18 and age <= 50:
    print("You're an adult.")
elif age >= 51:
    print("You're senior.")
else:
    print("invalid age") 