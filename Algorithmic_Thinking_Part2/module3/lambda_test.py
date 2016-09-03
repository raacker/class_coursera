import alg_cluster

def test():
    t = (10,3)

    print t
    for i in range(1,10):
        t = ((lambda x,y : (x,y) if x < y else (x, x-y))(i//3, i%3))
        print t


def test2():
    l = "hello"
    set_list = []
    for i in range(len(l)):
        set_list.append(set(l[i]))
    set_list = map(lambda x : set(x), l)
    print set_list


def test3():
    lists = [alg_cluster.Cluster(0,0,0,0,0)]*10

    print lists
test3()
