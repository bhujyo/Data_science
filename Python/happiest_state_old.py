import sys

import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

states_c = {key: (lambda x: states[x].upper())(key) for key in states}

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

def n_loc(X, n):
    l_lang = json.loads(open(X).readlines()[n]).get("lang")
    l_loc = json.loads(open(X).readlines()[n]).get("user")
    if l_lang != 'en':
        return None
    if l_loc is not None:
        l_loc = l_loc.get("location")
    if l_loc is None or l_loc == '':
        return None
    l_loc = [x.strip().upper() for x in l_loc.encode('utf-8').split(',')]
    for item in l_loc:
        if item in states:
            return states[item]
    return None
        
def sent_sc(X, Y, nn):
    sent_d = sentiment_dict(X)
    n_line = nthline(Y, nn)
    s_count = 0
    if n_line is not None:
        for word in n_line:
            if sent_d.get(word) is not None:
                s_count = s_count + int(sent_d.get(word))
    return s_count

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    ln = lines_num(tweet_file)
    st_list = []
    for i in range(ln):
        locn = n_loc(tweet_file, i)
        if locn is not None:
            ssc = sent_sc(sent_file, tweet_file, i)
            try:
                st_list.index(locn)[1] += ssc
                st_list.index(locn)[2] += 1
            except:
                st_list.append((locn, ssc, 1))
    n_st_list = [(entry[0], float(entry[1])/entry[2]) for entry in st_list]
    n_st_list.sort(key=lambda state: state[1], reverse=True)
    print n_st_list[0][0]

if __name__ == '__main__':
    main()

