import string
import praw
#from nltk.corpus import stopwords


r = praw.Reddit(user_agent='my scraper')

submissions = r.get_subreddit('shitredditsays').get_top(limit=10)

all_submis = []
for jarb in submissions:
    submission = jarb.comments
    all_submis.append(submission)

yaywords = []
for i in all_submis:
    for j in i:
        thing = str(j)
        yaywords.append(thing)


#texts = []
#for j in yaywords:
#    text = ' '.join([word for word in j.split() if word not in (stopwords.words('english'))])
#    texts.append(text)

cleantext = []
for x in yaywords:
    out = x.translate(string.maketrans("", ""), string.punctuation)
    cleantext.append(out)

with open('srs.txt', 'w') as corpora:
    for i in cleantext:
        corpora.write(i + '.' + '\n')
