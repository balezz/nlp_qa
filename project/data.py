import string

with open('../tests/text/prob_theory_10') as f:
    lines = f.readlines()
DATA = [s.split('-') for s in lines]

if __name__ == '__main__':
    print(DATA)
