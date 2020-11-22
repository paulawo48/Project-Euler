# create the sequence
def main(limit):
    lst = [1,2]
    num = 0
    while num < limit:
        num = sum(lst[-2:])
        lst.append(num)
    lst_clean = [x for x in lst if x < limit]    
    evens = [x for x in lst_clean if x % 2 ==0]
    total = sum(evens)
    return total

if __name__ == '__main__':
    total = main(4000000)
    print(total)
