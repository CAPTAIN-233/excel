def volt(a,b,c):
    n = []
    for i in range(0,int((b-a)/c)+1):
        #print('current is {0}'.format(x))
        n.append(round(a,2))
        a += c

    print(n)
    return a

def current(x,y,z):
    m = []
    for i in range(0,int((y-x)/z)+1):
        #print('current is {0}'.format(x))
        m.append(round(x,2))
        x += z

    #print(m)
    return m


if __name__ == '__main__':
    print(volt(0,20,2))