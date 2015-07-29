print("Input string: \n")
mystring = "The US and Turkey are working together on military plans to clear the Islamic State (IS) group from parts of northern Syria, American officials say.\nThey said an \"Islamic State-free zone\" would ensure greater stability along the Syria-Turkish border.\nThe talks follow a major shift in Turkey's approach to IS in recent days."
print(mystring)
print("\nNumber of character: %d"%(len(mystring)))
print("Number of word:  %d"%(len(mystring.split(" "))))
print("Number of sentence:  %d"% len(mystring.split(".")))
print("Number of paragraph:  %d"%(len(mystring.split("\n"))))
