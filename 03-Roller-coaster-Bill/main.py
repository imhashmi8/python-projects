print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Child Bill is {bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth Bill is {bill}")
    else:
        bill = 10
        print(f"Adult Bill is {bill}")

    want_photo = input("Do you want photo ? type 'Y' for Yes and 'N' for No : ")
    if want_photo == "Y":
        bill +=3

    print(f"Your Total bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

