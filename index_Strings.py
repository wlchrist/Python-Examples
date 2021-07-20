# You can also index strings, and find the position of a character

flavor = "apple pie"
print (flavor[1])

# remember, 1 isn't the first character but [0] is

print (flavor[0])

# Python also supports negative indexes. REMEMBER: -1 BEGINS AT THE LAST CHARACTER

negative_index = print(flavor[-1])
print(negative_index)

# Python also allows Substrings which can be used to identify a range of letters

sub_string = "Hello, my name is Warren. I really like apple pie"

range_of_string = sub_string[0:5]
print(range_of_string)
print(len(range_of_string)) # <-- put that in there because I can

# If you omit the first character of the substring length then python assumes you mean "0", or if you omit the end then
# It assumes you want the last character as well

omit_substring = sub_string[:5]
print(omit_substring)