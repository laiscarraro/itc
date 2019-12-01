import random, re, os

# freqDict is a dict of dict containing frequencies
def addToDict(fileName, freqDict):
	f = open(fileName, 'r')
	words = re.sub("\n", " \n", f.read()).lower().split(' ')

	# count frequencies curr -> succ
	for curr, succ in zip(words[1:], words[:-1]):
		# check if curr is already in the dict of dicts
		if curr not in freqDict:
			freqDict[curr] = {succ: 1}
		else:
			# check if the dict associated with curr already has succ
			if succ not in freqDict[curr]:
				freqDict[curr][succ] = 1;
			else:
				freqDict[curr][succ] += 1;

	# compute percentages
	probDict = {}
	for curr, currDict in freqDict.items():
		probDict[curr] = {}
		currTotal = sum(currDict.values())
		for succ in currDict:
			probDict[curr][succ] = currDict[succ] / currTotal
	return probDict

def markov_next(curr, probDict):
	if curr not in probDict:
		return random.choice(list(probDict.keys()))
	else:
		succProbs = probDict[curr]
		randProb = random.random()
		currProb = 0.0
		for succ in succProbs:
			currProb += succProbs[succ]
			if randProb <= currProb:
				return succ
		return random.choice(list(probDict.keys()))

def make(curr, probDict, T = 50):
	data = [curr]
	for t in range(T):
		data.append(markov_next(data[-1], probDict))
	return " ".join(data)

def modeler(dataset):
    dataFreqDict = {}
    files = os.listdir(dataset)
    
    for i in range(len(files)):
        dataProbDict = addToDict(dataset+files[i], dataFreqDict)

    startWord = input("Insira os acordes desejados: \n > ")
	
    output = make(startWord, dataProbDict, T = 60)
    
    print("Output criado com sucesso")
    
    return output