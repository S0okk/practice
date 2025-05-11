lines = ["Hello", "World", "Python", "Is", "Awesome"]
with open('output.txt','w') as file:
    for line in lines:
        
        file.write(line + '\n')
with open('output.txt', 'r') as file:
    print(len(file.readlines()))
