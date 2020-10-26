import sys
from collections import defaultdict
import collections
import string

def Ball_Drop(Heights, drop_num = 5):
    l = list()
    l2 = list()
    l.append(Heights)
    while drop_num>0:
        drop_num -= 1
        Heights *= 0.25
        l.append(Heights)
   # print(l)
    l2.append(l[0])
    l2.append(l[-1])
    for i in range(1,len(l)-1):
        l[i] *= 2
        l2.append(l[i])
  
    return sum(l2)


def Step_2_Fibo(Number, isIncrement = True):
    x = 0
    y = 1
    z = x+y
    
    if Number <= 0 or Number == 1 :
        return 0
    while z<Number:
        x = y
        y = z
        z = x+y
        #print("x: ",x, " "," y: ",y," "," z: ",z)
    if Number == z:
        return 0
    
    if isIncrement:
        return z-Number
    else:
        return Number-y


def Get_Token(sentence):
    count = collections.defaultdict(int)
    for i in sentence.split():
        words = i.lower()
        for punctuations in string.punctuation:
            words = words.replace(punctuations, "")
        count[words]+=1
        
    return dict(count)
    
def identi_Substring(test_string):
    length_string = len(test_string)
    if length_string == 0:
        return 0
    
    substr_count = 0
    
    x = 0
    y = x+1
    while y < length_string:
        if test_string[x] == test_string[y]:
            y+=1
        else:
            difference = y-x
            substr_count += (difference*(difference + 1))/2
            x, y = y, y+1
    remaining= length_string - x
    substr_count += (remaining * (remaining +1))/2
    return int(substr_count)
    

if __name__ == "__main__":
    print("\nQ1")
    ans_ls = []
    try:
        ans_ls.append(Ball_Drop(100, 2)==156.25)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Ball_Drop(10, 1)==12.5)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Ball_Drop(20)==33.30078125)
    except:
        ans_ls.append(False)

    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')



    print("\nQ2")
    ans_ls = []

    Given_str_1  = '''
    "No need to light a Night light on a Light night,\t like tonight!"
    '''
    Given_str_2  = '''
    How any good cookies could a good cook cook, if a good cook could cook as many good cookies\n as a good cook could cook?
    '''
    try:
        res_dict_1 = Get_Token(Given_str_1)
        ans_ls.append(res_dict_1 == {'no': 1, 'need': 1, 'to': 1, 'light': 3, 'a': 2, 'night': 2, 'on': 1, 'like': 1, 'tonight': 1})
    except:
        ans_ls.append(False)

    try:
        res_dict_2 = Get_Token(Given_str_2)
        ans_ls.append(res_dict_2 == {'how': 1, 'any': 1, 'good': 5, 'cookies': 2, 'could': 3, 'a': 3, 'cook': 6, 'if': 1, 'as': 2, 'many': 1})
    except:
        ans_ls.append(False)
    

    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')


    print("\nQ3")
    ans_ls = []
    try:
        ans_ls.append(Step_2_Fibo(15, False)==2)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Step_2_Fibo(15)==6)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Step_2_Fibo(21, True)==0)
    except:
        ans_ls.append(False)
    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')


    print("\nQ4")
    ans_ls = []
    try:
        #print(identi_Substring('zzzz'))
        ans_ls.append(identi_Substring('zzzz')==10)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(identi_Substring('zzzyz')==8)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(identi_Substring('zzxyzzz')==11)
    except:
        ans_ls.append(False)
    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')