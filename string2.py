print("Input string: \n")
mystring = "The US and Turkey are working together on military plans to clear the Islamic State (IS) group from parts of northern Syria, American officials say.\nThey said an \"Islamic State-free zone\" would ensure greater stability along the Syria-Turkish border.\nThe talks follow a major shift in Turkey's approach to IS in recent days."
print(mystring)
# count number of sentence in a string
def sentenceCounter(s):
	return len(s.split("."))

# count number of word in a string
def wordCounter(s):
	return len(s.split(" "))

# counter number of times a word appears in a string
def wordCounter2(w,s):
	counter=0
	wordArray = s.split(" ")
	for i in range(len(wordArray)):
		if wordArray[i] == w:
			counter+=1
	return counter
print("Number of word: %d"%(wordCounter(mystring)))
print("Number of sentence: %d"%(sentenceCounter(mystring)))

print("Give me the word to find:")
mw = input()
print("\nNumber of word %s: %d"%(mw,wordCounter2(mw,mystring)))
