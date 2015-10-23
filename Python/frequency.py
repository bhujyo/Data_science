import sys

import json

def l_num(X):
    fp = open(X)
    return len(fp.readlines())

def nthline(fp,n):
    lib = json.loads(fp.readlines()[n]).get("text")
    if lib is not None:
        lib_enc = lib.encode('utf-8')
        lib = lib_enc.split()
    return lib

def main():
    ln = l_num(sys.argv[1])
    word_list = []
    total_count = 0
    for i in range(ln):
        tweet_file = open(sys.argv[1])
        n_line = nthline(tweet_file, i)
        if n_line is not None:
            for item in n_line:
                total_count += 1
                try:
                    word_list.index(item)[1] += 1
                except:
                    word_list.append([item,1])
    for key,value in word_list:
        print key, value/float(total_count)
    
if __name__ == '__main__':
    main()
