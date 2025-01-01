# comms

## What it is
comms provides a simple interface for performing NLP related tasks.

## Sources
Many libraries helped with this. Specifically: `nltk`, `keras`, `tensorflow`, and `transformers`.

In order to be fair:

#### TensorFlow And Keras

Abadi, Martin and Barham, Paul and Chen, Jing and Chen, Zheng and Davis, Austin and Dean, Jeffrey and Devin, Mat and Ghemawat, Sanjay and Irving, Geoffrey and Isard, Michael et al. (2016), TensorFlow: A system for large-scale machine learning, OSDI 265-283, vol. 16

#### NLTK

Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

#### Transformers

Wolf, Thomas and Debut, Lysandre and Sanh, Victor and Chaumond, Julien and Delangue, Clément and Moi, Pierric and Cistac, Pierric and Ruder, Sebastian, et al. (2020), Transformers: State-of-the-art Natural Language Processing, arXiv:1910.03771

## Installation

`python setup.py install`

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

Polarity of some sentence.

```
python main.py polarity "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

0.25
```

## Sentiment

```
python main.py sentiment "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[{'neg': 0.0, 'neu': 0.725, 'pos': 0.275, 'compound': 0.2263}, {'neg': 0.219, 'neu': 0.781, 'pos': 0.0, 'compound': -0.2411}]
```

## Nouns / Noun Phrases

```
python main.py nouns "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[u'big fan']
```
