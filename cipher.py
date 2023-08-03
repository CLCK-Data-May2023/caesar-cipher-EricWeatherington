# add your code here
user_sentence = input("Please enter a sentence: ")
user_sentence = user_sentence.lower()
encoded_sentence = ""

regular_alp = ["a", "b", "c", "d", "e", 
"f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

shift5_alp = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"a", "b", "c", "d", "e"]

for i in user_sentence: 
    if i in regular_alp:
        encoded_sentence += shift5_alp[regular_alp.index(i)]
    else:
        encoded_sentence += i

print("The encrypted sentence is:", encoded_sentence)