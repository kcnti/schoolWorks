if __name__ == '__main__':
    score = []
    for _ in range(0,int(input())):
        score.append([input(), float(input())])

    secondHighest = sorted(list(set([marks for name, marks in score])))[1]
    print('\n'.join([a for a,b in sorted(score) if b == secondHighest]))