# You are a shepherd who owns a flock of sheep
# Each of your sheep of your flock has different size

# Create a list to represent the size of your flock
flock = [5, 7, 300, 90, 24, 50, 75]

# Print all of your flock size
print("Hello, my name is Giang and there are my ship sizes:")
print(flock) 

# At the end of each month, you have to choose one and only one sheep to shear and 
# thus you want to choose the biggest one to maximize your profit
# Search for the biggest sheep in my list
maxSize = max(flock)
print("Now my biggest sheep has size", maxSize,"let's shear it")

# When your biggest sheer, its size will return to the default size, which is 8
# Print out your ship size after sheering the biggest one
sheer = flock.index(maxSize)
flock [sheer] = 8
print ("After shearing, here is my flock")
print(flock)

total = 0

# In the following month, every sheep in your flock grow, they have their size increased by 50
for i in range(3):
    
    for j in range(len(flock)):
        flock[j]+=50
        if i==2:
            total += flock[j]
            print("Month", i+1, ":")
            print("One month has passed, now here is my flock")
            print(flock)


    while i<2:
        maxSize = max(flock)
        sheer = flock.index(maxSize)
        flock[sheer]=8
        print("Now my biggest sheep size",maxSize, "let's shear it")
        print("After shearing, here is my flock")
        print(flock)
        break

print("my flock size in total: ", total)
print("I would get: ", 2*total)



