# comms

## What it is
comms provides a simple interface for performing NLP related tasks.

## Sources
Many libraries helped with this. Specifically: `nltk`, `keras`, `tensorflow`, and `transformers`.

In order to be fair:

#### TensorFlow And Keras

Abadi, Martin and Barham, Paul and Chen, Jing and Chen, Zheng and Davis, Austin and Dean, Jeffrey and Devin, Mat and Ghemawat, Sanjay and Irving, Geoffrey and Isard, Michael et al. (2016), TensorFlow: A system for large-scale machine learning, OSDI 265-283, vol. 16

#### Question Answerer

Currently this library uses `TFDistilBertForQuestionAnswering` as a pipeline for answering questions.

```
"A transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data. It is used primarily in the fields of natural language processing (NLP) and computer vision (CV).Like recurrent neural networks (RNNs), transformers are designed to process sequential input data, such as natural language, with applications towards tasks such as translation and text summarization. However, unlike RNNs, transformers process the entire input all at once. The attention mechanism provides context for any position in the input sequence. For example, if the input data is a natural language sentence, the transformer does not have to process one word at a time. This allows for more parallelization than RNNs and therefore reduces training times. Transformers were introduced in 2017 by a team at Google Brain and are increasingly becoming the model of choice for NLP problems, replacing RNN models such as long short-term memory (LSTM). The additional training parallelization allows training on larger datasets. This led to the development of pretrained systems such as BERT (Bidirectional Encoder Representations from Transformers) and GPT (Generative Pre-trained Transformer), which were trained with large language datasets, such as the Wikipedia Corpus and Common Crawl, and can be fine-tuned for specific tasks."

python main.py answer_question "What pretrained systems were developed from parallelization", context
```

#### NLTK

Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

#### Transformers

Wolf, Thomas and Debut, Lysandre and Sanh, Victor and Chaumond, Julien and Delangue, Clément and Moi, Pierric and Cistac, Pierric and Ruder, Sebastian, et al. (2020), Transformers: State-of-the-art Natural Language Processing, arXiv:1910.03771

## Installation

`python setup.py install`

## Tokenization

There is straightforward tokenization within this library, where we can generate a BoW (Bag of Words) containing primary keys of each word within some corpus of text.

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
