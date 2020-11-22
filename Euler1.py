def main(value):
    values = list(range(1,value))
    
    tally = [x for x in values if x % 5 == 0 or x % 3 == 0]
    
    total = sum(tally)
    return total

if __name__ == '__main__':
    total = main(1000)
    print(total)