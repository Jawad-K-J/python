f = open("file1.txt","x")
f.close()
f = open("library.txt","w")
f.write("India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[24] is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar and Indonesia.")

f = open("library.txt","r")
data = f.read()
k = data.count("to")
print("Occurrences of the word 'to' is:",k)

f = open("library.txt","r")
data = f.read()
k = data.count("the")
print("Occurrences of the word 'the' is:",k)
f.close()
