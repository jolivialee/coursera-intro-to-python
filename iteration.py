# Prompt for a list which repeatedly reads numbers until the user enters "done". At the end print out both the maximum and minimum of the numbers. 

largest = None
smallest = None
num = None
counter = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if counter == 0:
            largest = num
            smallest = num
        counter = counter+1
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    except:
        print("Invalid input")

    

print("Maximum", largest)
print("Minimum", smallest)
