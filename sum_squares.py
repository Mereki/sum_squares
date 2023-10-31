def list_nums(n):
    lst = []
    for a in range(int(n**0.5)+1):
        na = n - a**2
        for b in range(a, int(na**0.5)+1):
            nb = na - b**2
            for c in range(b, int(nb**0.5)+1):
                nc = nb - c**2
                d = int(nc**0.5)
                if d**2 == nc:
                    lst.append(a)
                    lst.append(b)
                    lst.append(c)
                    lst.append(d)
                    if len(lst) == 4:
                        return lst
