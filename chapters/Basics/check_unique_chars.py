text = "The coursework can be found at https://coursework.com/all. Please contact the admin office based on the dates."

# compute the unique characters
chars = "".join(set(text))
print(chars)

# computer the dict
char_dict = {token: idx for (idx, token) in enumerate(chars)}
print(char_dict)