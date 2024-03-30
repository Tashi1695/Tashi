age = int(input("Enter age:"))
y = input("Are you student(yes/no):")

if age <= 12 :
    print("your eligible for a discount on the movie tickit.")
elif age > 13 and age < 18  and y == "yes":
    print("your eligible for a discout for the movie tickit.")
else :
    print("your not eligible for discount.")
