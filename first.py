print("Newton's second law.")
print("general law : F = ma ")
print ("select missing value: ")
print("1 mass (m)")
print("2 accleration (a)")
print("3 Force (F)")
missing_value_choice = input("enter option no.")
if missing_value_choice == "1":
    a = float(input("enter value of a:"))
    F = float(input("enter value of F:"))
    m = F / a
    print(f"mass (m)= {m}")
elif missing_value_choice == "2":
    m = float(input("enter value of m:"))
    F = float(input("enter value of F:"))
    a = F / m
    print(f"acceleration (a) = {a}")
elif missing_value_choice == "3":
    a = float(input("enter value of a:"))
    m = float(input("enter value of m:"))
    F = m * a
    print(f"force(F) = {F}")
else :
    print("invalid choice.")