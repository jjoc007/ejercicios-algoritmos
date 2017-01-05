from multiprocessing import Pool

def f(x,y):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [[1,2], [2,3]]))