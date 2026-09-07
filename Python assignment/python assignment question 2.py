fruits = ["Pear","Apple", "Grapes", "Mango","Banana"]
with open("fruits.txt","w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")
with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())
