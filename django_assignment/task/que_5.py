def aggregate_count(data, key):
    c = 0
    print('111111')
    for i in data:
        print(2222)
        for j in i:
            print(3333)
            if j == key:
                c += 1
    return c


def aggregate_sum(data, key):
    s = 0
    for i in data:
        for j in i:
            if j == key:
                s += i[j]

    return s


def aggregate_avg(data, key):
    a = []
    s = 0
    print("iiii")
    for i in data:
        for j in i:
            if j == key:
                a.append(i[j])
                s += i[j]
    return s/len(a)


def aggregate_max(data, key):
    a = []
    for i in data:
        for j in i:
            if j == key:
                a.append(i[j])
    return max(a)


def aggregate_min(data, key):
    a = []
    for i in data:
        for j in i:
            if j == key:
                a.append(i[j])
    return min(a)

