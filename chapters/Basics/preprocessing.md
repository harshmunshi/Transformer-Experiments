# Basic Preprocessing in NLP

The following are important preprocessing steps for any NLP tasks:

## Defining a dictionary

Depending on your task, you would need or not need digits, hyperlinks or any other special characters. Understand the requirements and make the dictionary accourdingly.

Consider this example text
```
The coursework can be found at https://coursework.com/all. Please contact the admin office based on the dates.
```

has the following unique character set:
```
cwn.f/ld uhb:pamktTiProes
```

So your dictionary should contain indexed character list given by the set.

## Tokenisation

Extending the previous example, we can define tokens in the dictionary as follows:

```
unique_chars = "cwn.f/ld uhb:pamktTiProes"
char_dict = {token: idx for (idx, token) in enumerate(unique_chars)}
```

which means, now we can tokenise the following characters to

```
"The"
["t", "h", "e"]
[17, 5, 12]
```

This now can be used in case of NNs since it can only understand numbers.

## NOTE

The examples given for preprocessing are basically "character" level. It can also be done at word level which I will (also) in other examples.