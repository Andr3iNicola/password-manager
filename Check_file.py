import os

if os.stat('filekey.key').st_size == 0:
    key_file = False
else:
    key_file = True

with open('data.txt','r') as d:
    d.seek(0)
    first_char = d.read(1)
    if not first_char:
        file=True
    else:
        file=False

















