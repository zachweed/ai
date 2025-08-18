# ai

## What it is
ai provides an interface for performing NLP related tasks. Assuming we have "a paragraph" as a string of characters, there are two approaches: simple and complex.

### Simple
One can provide a sentence of characters and call things like `#polarity` to determine how 'positive' a sentence is. 

### Complex
One could encode the vector as a paragraph in `Dictionary`. Likewise, if someone wanted to the could represent two 'dictionaries' of vectorized strings in a high-dimensional space for performing linear algebra and calculus operations on the data.

## Installation

`python setup.py install`

## Knowledge Base

Given some context, and a question, we can receive an answer to said question with this library.

```bash
$ CONTEXT="Underground hiphop is a genre of hiphop that comprises non-commercialized patterns of music, including concepts like: lo-fi, heavy sampling, limited releases, etc. Many are not aware of underground hip-hop as a genre, as it is like the special reserve of commercialized artists. Having said that, many of the commercialized artists have gone on to influence a lot of the artists that we know today."

$ python main.py answer_question "What genre of artists were influenced by underground hiphop artists?", "$CONTEXT"
Answer: 'commercialized', score: 0.2764, start: 309, end: 323

$ python main.py answer_question "Are many away of underground hiphop as a genre?", "$CONTEXT"
Answer: 'Many are not aware', score: 0.2839, start: 164, end: 182

$ python main.py answer_question "Is there a genre that has underground in the name?, "$CONTEXT"
Answer: 'Underground hiphop', score: 0.7883, start: 0, end: 18

$ python main.py answer_question "Commercial hiphop artists were influence by what genre of artists?", "$CONTEXT"
Answer: 'Underground hiphop', score: 0.2537, start: 0, end: 18
```


## Tokenization

There is tokenization within this library, where we can generate a BoW (Bag of Words) containing primary keys of each word within some corpora.

```
python main.py tokenize "I am a person"
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
python main.py translate "translate from English to French: What is life like"

quoi ressemble la vie?
```
### German
```
python main.py translate "translate from English to German: What is life like"

Wie sieht das Leben aus?
```

## Polarity

Polarity of some sentence, meaning what the overall sentiment of some sentence is.

```
python main.py polarity "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

0.25
```

## Sentiment
This is where this library started. So, we can determine how positive, negative, neutral, and overall of each some sentence is.
```
python main.py sentiment "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[{'neg': 0.0, 'neu': 0.725, 'pos': 0.275, 'compound': 0.2263}, {'neg': 0.219, 'neu': 0.781, 'pos': 0.0, 'compound': -0.2411}]
```

## Nouns / Noun Phrases

```
python main.py nouns "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[u'big fan']
```

## Sources

Many libraries helped with this. Specifically: `nltk`, `keras`, `tensorflow`, `huggingface` (as a service), and `transformers`.
