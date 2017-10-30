# jint

## Installation

`python setup.py install`

## Sentiment

```
python main.py sentiment "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[{'neg': 0.0, 'neu': 0.725, 'pos': 0.275, 'compound': 0.2263}, {'neg': 0.219, 'neu': 0.781, 'pos': 0.0, 'compound': -0.2411}]
```

## Nouns / Noun Phrases

```
python main.py sentiment "Are you okay with eating oatmeal? I'm normally not a big fan of it myself."

[u'big fan']
```
