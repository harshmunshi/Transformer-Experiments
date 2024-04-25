# load the text file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# unique characters
chars = sorted(list(set(text)))
vocab_size = len(chars)
print("".join(chars))
print(vocab_size)