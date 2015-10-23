import sys

import json

def l_num(X):
    fp = open(X)
    return len(fp.readlines())

def n_htag(fp,n):
    ents = json.loads(fp.readlines()[n]).get('entities')
    if ents is not None:
        htgs = ents.get('hashtags')
    else:
        htgs = []
    l_htg = len(htgs)
    htg_l = []
    if l_htg > 0:
       for i in range(l_htg):
           htg_l.append(htgs[i].get('text').encode('utf-8'))
    return htg_l
           
def main():
    ln = l_num(sys.argv[1])
    htag_list = []
    for i in range(ln):
        tweet_file = open(sys.argv[1])
        n_tag = n_htag(tweet_file,i)
        if n_tag != []:
            for tag in n_tag:
                try:
                    htag_list.index(tag)[1] +=1
                except:
                    htag_list.append((tag,1))
    htag_list.sort(key=lambda tag: tag[1], reverse=True)
    l_htag = len(htag_list)
    if l_htag > 10:
        htag_list = htag_list[0:10]
    for key,value in htag_list:
        print key, value
    
if __name__ == '__main__':
    main()
