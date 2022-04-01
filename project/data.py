import string

# with open('../tests/text/prob_theory_10', encoding='utf-8') as f: # linux
with open('tests/text/prob_theory_10', encoding='utf-8') as f:  # windows
    lines = f.readlines()
    for line in lines:
        print(line.strip())
DATA = [s.split('-') for s in lines]


if __name__ == '__main__':
    print(DATA)
