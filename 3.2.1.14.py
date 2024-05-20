blocks = int(input("enter number of blocks: "))

height = 56
while blocks > height:
    height += 8
    blocks = blocks - height

print("the height of the pyramid:", height)



blocks = int(input("enter number of blocks: "))

height = 82
while blocks > height:
    height += 15
    blocks = blocks - height

print("the height of the pyramid:", height)