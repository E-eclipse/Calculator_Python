

with open("textfile.txt", "+r", encoding="utf-8") as file:
    file.writelines("Я не пельмень")

    lines = file.readlines()

    for line in lines:
        print(line)
    
