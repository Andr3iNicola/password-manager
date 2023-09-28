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


"""with open('filekey.key','r') as k:
    readline=k.readlines()
    lenght=len(readline[0])

    if lenght == 44:
        key_file=True
    else:
        key_file=False

print(key_file)"""















