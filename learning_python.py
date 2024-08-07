file_name = 'learning_python.txt'
with open(file_name)as file_obejct:
    text = file_obejct.readlines()

for line in text:
    print(line.replace('python', 'C'))
    # print(line)
