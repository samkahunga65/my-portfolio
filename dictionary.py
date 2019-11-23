import json
import time
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))

def close_matches(val):
    doppelganger = get_close_matches(val, data.keys(), n=2)
    return doppelganger[0]

def check_word(val):
    # if data[val] == True:
    #        return data[val]
    # else:
    #     r = close_matches(val)
    #     print(f'did you mean: {r}')
    #     return data[r]
    try:
        return data[val]
    except:
        r = close_matches(val)
        print(f'did you mean: {r}')
        return data[r]

vv = 1
while vv == 1:
    x = input('enter the word whos definition you want to get: ')
    cw = check_word(x)
    # print(type(cw))
    # vv = 'vag'
    if type(cw) == list:
        print(cw)
        time.sleep(3)
        y = input('would you like to continue? y/n ')
        if y.lower() == 'y':
            continue
        elif y.lower() == 'n':
            print('y u do dat?')
            vv = 'vag'
            break
        else:
            print('and wee are outta here')
            vv = 'vag'
            break
    else:
        print('no such word please try again'.upper())
        time.sleep(2)
        continue
