import os, time

print(time.localtime(os.stat('problem_1.py').st_mtime))
