from datetime import datetime
import time
print(datetime.now())

d1 = datetime.now()
print("d1=", d1)
time.sleep(1)
d2 = datetime.now()
print("d2=", d2)

print(d2 - d1, sep=',')