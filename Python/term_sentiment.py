import sys

import json

def lines_num(X):
    fp = open(X)
    return len(fp.readlines())

def nthline(X, n):
    lib = json.loads(open(X).readlines()[n]).get("text")
    if lib is not None:
       lib = lib.split()
    return lib

def sentiment_dict(X):
    X = open(X)
    scores = {}
    for line in X:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return dict(scores.items())


def sent_sc(sent_file, tweet_file, nn):
    sent_d = sentiment_dict(sent_file)
    n_line = nthline(tweet_file, nn)
    count_p = 0.
    count_n = 1.
    term = []
    if n_line is not None:
        for word in n_line:
            ssc = sent_d.get(word)
            if ssc is not None:
                if ssc > 0:
                   count_p += abs(ssc)
                elif ssc < 0:
                   count_n += abs(ssc)
            else:
                term.append(word.encode('utf-8'))
        term = list(set(term))
        s_count = float(count_p)/count_n
    return [(x, s_count) for x in term]

def main():
    ll = lines_num(sys.argv[2])
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    terms = []
    for i in range(10):
        x = sent_sc(sent_file, tweet_file, i)
        if x != []:
            for item in x:
                try:
                    terms.index(item[0])[1] += item[1]
                except:
                    terms.append(item)
    for key, value in terms:
        print key, value

if __name__ == '__main__':
    main()
