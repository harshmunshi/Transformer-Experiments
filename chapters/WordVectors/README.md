# Word Vectors (Embeddings)

Word vectors as the name suggests, is a higher dimensional mathematical representation of the "meaning" of the word.

* A mathematical attempt to represent word meanings.
* Semantically close words will occupy nearby places in the vector space.
* NOTE: Sematical closeness does not mean the understanding of grammar. For example consider the following sentences

```
A mole of carbon.
Getting the mole tested.
```

* The word "mole" might have the same embedding, but it differs in meaning.

## Types of Words Vectors

The word vectors can be divided into three major parts:

- tf-idf (Document Level)
- Bag of Words (Document Level)
- Word2Vec (Corpus Level)
- GloVe (Corpus Level)
- Many more (post transformers)

## Explanation for Word2Vec

Developed by Google in 2013. The idea is to define an NN that has a fixed length inputs and outputs. It iterates over a corpus of a text and learns a representation. The implementation can be done in one of two ways:

* CBOW (continuous bag of words)
* Skip-Gram

CBOW model predicts the target word from the surrounding context.
Skip-gram predicts the surrounding context from the target word.

### Similarity Metric
Cosine similarity