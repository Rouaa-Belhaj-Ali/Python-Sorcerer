import subprocess
import time
import os

with open ("program.py","w") as file:
    file.write('print("hello,world!")')

print  ("preparing to run file")
time.sleep(1)

subprocess.call(["python","program.py"])
time.sleep(1)


print('removing  "program.py"')
time.sleep(1)

os.remove("program.py")