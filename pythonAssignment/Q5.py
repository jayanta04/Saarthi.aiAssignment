import itertools
Entities_list = ["     kolkata", "delhi","mumbai","kolkata   "]
Utterance_list = ["How far is <> from <>    ", "How is the weather in <>","From <> to <> to <>"]

def data_cleanup(dataList):    
    dataList = [str.strip() for str in dataList]
    dataList = list(set(dataList)) 
    return dataList

def generate_utterances(entityList,utteranceList):
    entityList = data_cleanup(entityList)
    utteranceList = data_cleanup(utteranceList)
    resList = []
    for str in utteranceList:
        nullCount = str.count("<>") 
        entityPermutations = list(itertools.permutations(entityList,nullCount)) 
        for permutation in entityPermutations: 
            tempStr = str[:]
            for entity in permutation: 
                tempStr = tempStr.replace('<>',entity,1)
            resList.append(tempStr)
    return resList
        
all_unique_utterances = generate_utterances(Entities_list,Utterance_list)
print(all_unique_utterances)