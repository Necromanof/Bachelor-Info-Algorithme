def permutations(x):

    if not x:
        return[]
    
    liste = []
    liste.append(x[0])

    for i in range(1, len(x)):
        for j in reversed(range(len(liste))):
            delete = liste.pop(j)
            for k in range (len(delete) + 1):
                liste.append(delete[:k] + x[i] + delete[k:])

    print(liste, end='')

if __name__ == '__main__':
    x= 'ABC'
    permutations(x)
  

