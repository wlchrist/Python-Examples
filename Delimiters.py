# Delimiters are used to mark where the string begins and ends

string = "I have to leave"
print(string)
# In this case, the delimiter is a double quote

single_quote = 'She said, "I need to order some cake"'

print(single_quote)
# If you want to use the same type of quotation mark you can use a backslash like this:

both_quotes = "She said, \"I need to order some cake\""

print(both_quotes)

# Python has a built in length function

number_string = "1234"
len_function = len(number_string)
print(len_function)

# You can also triple quote a string to have whitespace like this

triple_quote_line = """Hello, my name is warren. 
    This is my demonstration of triple quotes to show
        that it can also include indents."""

print(triple_quote_line)

# To put a long string on one line, you can do this (Doesn't look like its working, come back later)
    long_string = "Hi my name is Warren. I like ice cream, white claws \
    , and having a good time"

    print(long_string)