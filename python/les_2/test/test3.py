def resheto(a):
    mass = []
    for i in range(2, a):
        mass.append(i)
    fin = []
    not_good = []
    for z in mass:
        for k in range(z+1, a):
            if k % z != 0 and k not in not_good:    # and k not in fin
                fin.append(k)
            elif k in not_good:
                continue
            elif k in fin:
                fin.remove(k)
                not_good.append(k)
            else:
                not_good.append(k)


    return fin

print(set(resheto(26)))
