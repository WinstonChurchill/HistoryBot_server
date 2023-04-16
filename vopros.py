from BasDat import BasaDate
from copy import copy, deepcopy

import random
import datetime

def vopros(date, seed=0):
    if seed == 0:
        seed = generate_seed_non()
    else:
        seed = seed.split('.')
        if len(seed) != 4:
            seed = generate_seed(str(seed))
        else:
            preobr_seed(seed)
    if int(seed[2]) > 100:
        seed[2] = 100
    return form_vopros(int(seed[2]), opros_alf(seed[1], date), int(seed[3]), int(seed[0])), '.'.join(map(str, seed))

def preobr_seed(seed):
    if seed[0] not in '12':
        a = 0
        for i in seed[0]:
            if i in '0123456789':
                a += int(i)
            else:
                a += ord(i)
        if a % 2 == 0:
            seed[0] = 1
        else:
            seed[0] = 2
    if seed[1].isdigit():
        pass
    else:
        a = 0
        for i in seed[1]:
            if i in '0123456789':
                a += int(i)
            else:
                a += ord(i)
        seed[1] = str(a)
    if seed[2].isdigit() and str(seed[2]) != '0':
        pass
    else:
        a = 0
        for i in seed[2]:
            if i in '123456789':
                a += int(i)
            else:
                a += ord(i)
        seed[2] = a
    if seed[3].isdigit():
        pass
    else:
        a = 0
        for i in seed[3]:
            if i in '0123456789':
                a += int(i)
            else:
                a += ord(i)
        seed[3] = a
    return seed

def generate_seed(seed):
    final_seed = []
    sum = 0
    for i in seed:
        sum += ord(i)
    if sum % 2 == 0:
        final_seed.append(1)
    else:
        final_seed.append(2)
    random.seed(sum)
    key = ['2', '3', '4', '5', '6', '7', '2', '3', '4', '5', '6', '7']
    a = []
    for i in range(random.randint(1, 7)):
        b = random.choice(key)
        key.remove(b)
        a.append(b)
    a = ''.join(a)
    final_seed.append(a)
    final_seed.append(random.randint(5, 30))
    final_seed.append(random.randint(0, 1000000))
    return final_seed

def generate_seed_non():
    seed = []
    seed.append(random.randint(1, 2))
    key = ['2', '3', '4', '5', '6', '7', '2', '3', '4', '5', '6', '7']
    a = []
    for i in range(random.randint(1, 7)):
        b = random.choice(key)
        key.remove(b)
        a.append(b)
    a = ''.join(a)
    seed.append(a)
    seed.append(random.randint(5, 30))
    now = datetime.datetime.now()
    seed.append(now.strftime('%f'))
    return seed

def form_vopros(col, date, seed, kakform):
    finality = {}
    datecops = deepcopy(date)
    b = list(date)
    for i in range(col):
        seed += 100
        random.seed(seed)
        random.shuffle(b)
        if len(date) > 1:
            a = random.choice(b)
        else:
            a = b[0]
        ff = list(datecops[a])
        if len(ff) == 4:
            datecops[a] = deepcopy(date[a])
        random.seed(seed)
        random.shuffle(ff)
        datecops[a].pop(ff[0])
        if kakform == 2:
            finality[ff[0]] = []
            finality[ff[0]].append(date[a][ff[0]])
            finality[ff[0]].append(date[a][ff[1]])
            finality[ff[0]].append(date[a][ff[2]])
        elif kakform == 1:
            finality[date[a][ff[0]]] = []
            finality[date[a][ff[0]]].append(ff[0])
            finality[date[a][ff[0]]].append(ff[1])
            finality[date[a][ff[0]]].append(ff[2])

    return finality

def opros_alf(seeds, date):
    opros = {}
    if int(seeds) == 1:
        opros = date
    else:
        random.seed(seeds)
        seeds = str(seeds).replace('1', '')
        seeds = str(seeds).replace('0', '')
        if len(seeds) == 0:
            key = ['2', '3', '4', '5', '6', '7', '2', '3', '4', '5', '6', '7']
            a = []
            for i in range(random.randint(1, 7)):
                b = random.choice(key)
                key.remove(b)
                a.append(b)
            seeds = ''.join(a)
        a = 1
        for g in date:
            a += 1
            if str(a) in seeds:
                opros[g] = date[g]
    return opros

if __name__ == '__main__':
    Dates = BasaDate()
    print(vopros(Dates.return_basa_date(), '1.0.0.1'))