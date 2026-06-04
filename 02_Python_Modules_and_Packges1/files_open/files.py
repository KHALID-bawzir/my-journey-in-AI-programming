import fileinput
import json
file = open('data.txt', 'w')
file.write('my name khalid and its a good name \n')
file.write('my name khalid and its a good name 2 \n')
file.close()

with open('data.txt', 'a') as f:
    f.write('my name khalid and its a good name with \n')

with open('asia.txt', 'r') as f:
    all = [ a.strip() for a in f.readlines()]
    print(all)

with open('asia.txt', 'r') as rf , open('asia2.txt', 'w') as wf :
    wf.write(rf.read())

with fileinput.input(files=('asia.txt','Africa.txt')) as f:
    index = 1
    for line in f:
        if fileinput.isfirstline():
            print(f'\n\n --- Reading {fileinput.filename()} ---')
            index = 1
        print(f'{index}-- {line}' , end='')
        index += 1

with open('data.json','r') as dj:
    data = json.load(dj)
    print(data)
