import spacy
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# load the english model
en_model = spacy.load("en_core_web_sm")

# words
words = "apple banana jackfruit lion"
word_list = ["apple", "banana", "jackfruit", "lion"]
word_tokens = en_model(words)
pca = PCA(n_components=2)

# list of vectors
vec_list = []
# visualise the tokens
for i in range(len(word_tokens)):
    vector = word_tokens[i].vector
    vector = vector.reshape(96, 1)
    vec_list.append(vector)

# Veclist -> array
vector_array = np.asarray(vec_list).reshape(-1, 96)
# take the pca
pca_vectors = pca.fit_transform(vector_array)

# plot the vectors
for i in range(4):
    vector_2d = pca_vectors[i, :]
    plt.scatter(vector_2d[0], vector_2d[1])
    plt.annotate(text=word_list[i], xy = (vector_2d[0], vector_2d[1]))
plt.show()