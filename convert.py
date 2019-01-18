import json

file1 = open('widgets.json')
js = json.load(file1)
op = open('op.json','w')

def getStr(element):
    s = '"' + element['name'] + '" : ' + '{"desc": "' + element['description'] + '","url": "' + element['link'] + '"},'
    return s

for element in js:
    op.write(getStr(element))

op.close()
file1.close()
