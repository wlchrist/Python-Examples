# In Python, you can also find a String, within a string
# Pretty cool

sentence = "Here in my garage"
print(sentence.find("garage"))
# This will print the index location of "garage"
# There is also a .replace() method that we can use to well, replace stuff in a string like this

truth = "I tell the truth and nothing but the truth!"
print(truth)
lies = truth.replace("the truth", "lies")
print(lies)