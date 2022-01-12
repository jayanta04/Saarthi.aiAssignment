d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


def mergeDictionary(d1,d2):
    if len(d1) < len(d2):  
        d1,d2 = d2,d1
    newDictionary = d1.copy()   
    for key,value in d2.items():
        if key in d1.keys():
            newDictionary[key] = newDictionary[key] + value
        else:
            newDictionary[key] = value

    return newDictionary

for key,value in mergeDictionary(d1,d2).items():
    print(key,':',value)