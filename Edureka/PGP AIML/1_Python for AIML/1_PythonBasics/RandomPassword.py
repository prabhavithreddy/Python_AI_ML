import random
import string
p_list = []
for i in range(1,11):
    p_list.append(random.choice(string.ascii_uppercase+ string.ascii_lowercase+string.digits))
password = ''.join(p_list)
print(password)