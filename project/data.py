with open('../tests/text/prob_theory_10.txt', encoding='utf-8') as f: # linux
    lines = f.readlines()

DATA = [s.split('-') for s in lines]


if __name__ == '__main__':
    print(DATA)
