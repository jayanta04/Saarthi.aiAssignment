dictList=[{'name': 'affirm', 'confidence': 0.9448149204254}, 
{'name': 'affirm', 'confidence': 0.944814920425415}, 
{'name': 'inform', 'confidence': 0.9842240810394287}, 
{'name': 'inform', 'confidence': 0.9842240810394287}]


def uniqueDict(dict):
    keyList = list(dictList[0].keys())
    firstKey = keyList[0]
    return {x[firstKey]:x for x in dictList}.values()

print(uniqueDict)
