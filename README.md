# ai

## What it is
ai provides an interface for performing NLP related tasks. Assuming we have "a paragraph" as a string of characters, there are two approaches: simple and complex.

### Simple
One can provide a sentence of characters and call things like `#polarity` to determine how 'positive' a sentence is. 

### Complex (non-ML)
One could encode the vector as a paragraph in `Dictionary`. Likewise, if someone wanted to the could represent two 'dictionaries' of vectorized strings in a high-dimensional space for performing linear algebra and calculus operations on the data.

### Complex (ML)

One could also work with the library in a way where they are interacting with things in a ML-oriented fashion. Meaning, rather than merely analyzing sentiment, they can work with a specific strategy of analyzing sentiment (e.g. Ensemble Learning).

## Installation

`% python setup.py install`

* In the event that any modules are missing (`ModuleNotFoundError`), one can always manually install via `pip install _module_name_`


## Sentiment
This is where this library started. So, we can determine how positive, negative, neutral, and overall of each some sentence is. What is returned is an object containing individual scores for each dimension of sentimentality.
```
% python main.py sentiment "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[{'neg': 0.0, 'neu': 0.725, 'pos': 0.275, 'compound': 0.2263}, {'neg': 0.219, 'neu': 0.781, 'pos': 0.0, 'compound': -0.2411}]
```

Having said that, eventually it transformed to where we provided, trained, and persisted a model such that we can determine sentiment from in-house trained data, in a way that shall increase in accuracy continously, and simplifies the sentiment for the consumer of the API. This is accomplished via an Ensemble Learning method comprising Logistic Regression, a SVM, and Näive Bayes. From there we can conditionally either ensembly by Stacking, or Voting the results. While this code can be called manually, the public interface can be called like so:

```
% python main.py overall_sentiment "We loved it"
['pos']

% python main.py overall_sentiment "We did not like it"
['neg']

% python main.py overall_sentiment "Wow it was amazing"
['pos']
```

## Knowledge Base

Given some context, and a question, we can receive an answer to said question with this library.

```bash
% CONTEXT="Underground hiphop is a genre of hiphop that comprises non-commercialized patterns of music, including concepts like: lo-fi, heavy sampling, limited releases, etc. Many are not aware of underground hip-hop as a genre, as it is like the special reserve of commercialized artists. Having said that, many of the commercialized artists have gone on to influence a lot of the artists that we know today."

% python main.py answer_question "What genre of artists were influenced by underground hiphop artists?", "$CONTEXT"
Answer: 'commercialized', score: 0.2764, start: 309, end: 323

% python main.py answer_question "Are many away of underground hiphop as a genre?", "$CONTEXT"
Answer: 'Many are not aware', score: 0.2839, start: 164, end: 182

% python main.py answer_question "Is there a genre that has underground in the name?, "$CONTEXT"
Answer: 'Underground hiphop', score: 0.7883, start: 0, end: 18

% python main.py answer_question "Commercial hiphop artists were influence by what genre of artists?", "$CONTEXT"
Answer: 'Underground hiphop', score: 0.2537, start: 0, end: 18
```

## Lab

There is a Lab defined that accepts a Dictionary of words. In terms of the dictionary of words, this is usually two corpora of text, where we fit a Vectorizer with the shared vocabulary from one corpus, transform it in relation to the second corpus, and resulting from this we have two points (encoded vectors) that we can place in a high-dimensional space (the Lab) where we can determine euclidean and cosine similarity. 

```
string_one = "hello I am a human"
string_two = "hello I am not a human but a man-like creature"

dictionary = Dictionary().fits(string_one)

x_one = dictionary.encoded_vector
x_two = dictionary.transform(string_two)

lab = Lab(x_one, x_two)

lab.euclidean()

3.6055
```

## PCA


## Tokenization

There is tokenization within this library, where we can generate a BoW (Bag of Words) containing primary keys of each word within some corpora.

```
% python main.py tokenize "I am a person"
I:      1
am:     2
a:      3
person: 4
{'I': 1, 'am': 2, 'a': 3, 'person': 4}
```

## Translation

Translate some string of text. Some variety of languages can be provided. For example: both `German` and `French` work. If there is an unsupported language, leave an issue and we can get it resolved and/or added within.

### French

```
% python main.py translate "translate from English to French: What is life like"

quoi ressemble la vie?
```
### German
```
% python main.py translate "translate from English to German: What is life like"

Wie sieht das Leben aus?
```

## Polarity

Polarity of some sentence, meaning what the overall sentiment of some sentence is.

```
% python main.py polarity "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

0.25
```

## Nouns / Noun Phrases

```
% python main.py nouns "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[u'big fan']
```

## Sources

Many libraries helped with this. Specifically: `nltk`, `keras`, `tensorflow`, `huggingface` (as a service), and `transformers`.
