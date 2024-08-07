file_name = 'pi_digits.txt'

full_line = ""
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    full_line += line.strip()

print(full_line)
print(len(full_line))
    