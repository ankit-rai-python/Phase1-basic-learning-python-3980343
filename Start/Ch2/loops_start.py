# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while x < 5:
    print(f"Current value of x: {x}")
    x += 1  # increment x by 1

answer = input("Shoud I stop? (yes/no) ")
# while answer.lower() != "yes":
#     print("Continuing the loop..." + answer)edye
#     answer = input("Shoud I stop? (yes/no) ")

# define a for loop
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    print(f"Today is {day}")


# use a for loop over a collection


# use the break and continue statements
for day in days:
    if day == "Wednesday":
        print("It's hump day!")
        continue
    print(f"Today is {day}")

# using the break statement to exit a loop early
for day in days:
    if day == "Tuesday":
        print("It's the weekend soon!")
        break  # exit the loop when we reach Friday
    print(f"Today is {day}")

# using the enumerate() function to get an index and an item
for index, day in enumerate(days):
    print(f"Day {index + 1}: {day}")

