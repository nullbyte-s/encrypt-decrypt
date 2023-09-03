import os
import random
import string
from datetime import datetime

home_dir = os.path.expanduser("~")
index_file = os.path.join(home_dir, "Projects", "encrypt-decrypt", "index.html")
log_file = os.path.join(home_dir, "Projects", "encrypt-decrypt", "log.txt")

with open(index_file, "r") as file:
    lines = file.readlines()

input_line = None
for i, line in enumerate(lines):
    if 'name="key"' in line:
        input_line = i
        break

if input_line is not None:
    line = lines[input_line]
    value_start = line.find('value="') + len('value="')
    value_end = line.find('"', value_start)
    current_value = line[value_start:value_end]
else:
    print("Linha <input type=\"hidden\" name=\"key\" id=\"key\" value=\"...\" /> não encontrada.")
    exit(1)

new_value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))

current_date = datetime.now().strftime("%d/%m/%Y")

if input_line is not None:
    lines[input_line] = line[:value_start] + new_value + line[value_end:]
    with open(index_file, "w") as file:
        file.writelines(lines)

else:
    print("Linha <input type=\"hidden\" name=\"key\" id=\"key\" value=\"...\" /> não encontrada.")

lines[-1] = current_date + " - " + current_value + "\n"
with open(log_file, "w") as file:
    file.writelines(lines[-1])