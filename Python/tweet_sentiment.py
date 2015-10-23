import sys

import json

def lines_num(X):
    fp = open(X)
    return len(fp.readlines())

def nthline(fp,n):
    lib = json.loads(fp.readlines()[n]).get("text")
    if lib is not None:
       lib = lib.split()
    return lib

def sentiment_dict(X):
    scores = {}
    for line in X:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return dict(scores.items())


def side(sent_file, tweet_file, nn):
    sent_d = sentiment_dict(sent_file)
    n_line = nthline(tweet_file, nn)
    s_count = 0
    if n_line is not None:
        for word in n_line:
            if sent_d.get(word) is not None:
                s_count = s_count + int(sent_d.get(word))
    print s_count

def main():
    ll = lines_num(sys.argv[2])
    for i in range(ll):
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])
        side(sent_file, tweet_file, i)
  
if __name__ == '__main__':
    main()
