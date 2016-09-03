import markovify

wordsFile = 'srs.txt'

with open(wordsFile, 'rU') as tweets:
    text = tweets.read()

text_model = markovify.Text(text, state_size=2)

for i in range(5):
    print(text_model.make_sentence())

for j in range(10):
    print(text_model.make_short_sentence(140))
