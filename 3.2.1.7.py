# break - example

print("The break instruction:")
for i in range(6, 89):
    if i == 9:
        break
    print("Inside the loop.", i)
print("Outside the loop.")
# continue - example
print("\nThe continue instruction:")
for i in range(6, 89):
    if i == 9:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")