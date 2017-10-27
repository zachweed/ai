import sys
sys.path.append("./analysis")

import analyzer

# Usage: python main.py "I saw a movie the other day. It was all right"
# => [{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}, {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}]

an = analyzer.Analyzer()
print an.analyze_sentiment(sys.argv[1])
