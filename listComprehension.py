def lists(x,y,z,n):
    #first line returns a list of arrays, for every possible value that can be taken
    list = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
    #second line filters them away if they add to n
    list = [x for x in list if x[0]+x[1]+x[2] != n]
    return list

if __name__ == '__main__':
    x = int(input("input x: "))
    y = int(input("input y: "))
    z = int(input("input z: "))
    n = int(input("input n: "))
    print(lists(x,y,z,n))

