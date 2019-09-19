first=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']
listcount=0
max=0
for z in first:
    if isinstance(z,list):
        listcount+=1
        if max < len(z):
            max=len(z)
            index=first.index(z)
print(listcount)
print(first[index])
print(index)
print([index][0])