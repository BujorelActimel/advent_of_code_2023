import re
from math import gcd

def parse(filename):
    s = open(filename).read().strip()
    cmd, body = s.split('\n\n')
    dic = {}
    for b in body.split('\n'):
        x,y,z = re.findall('\w+', b)
        dic[x] = [y, z]
    return cmd, dic

def runner(cmd, dic, start):
    i, stack = 0, [start]
    while 1:
        head = stack.pop()
        stack.append(dic[head][0] if cmd[i]=='L' else dic[head][1])
        i = (i+1) % len(cmd)
        yield head

# def part1(cmd, dic):
#     answer = 0
#     g = runner(cmd, dic, 'AAA')
#     while next(g)!='ZZZ':
#         answer += 1
#     print(answer)

def part2(cmd, dic):
    As = [key for key in dic.keys() if key[-1]=='A']
    gens = [runner(cmd, dic, A) for A in As]
    answer = 1
    for g in gens:
        rounds = 0
        while next(g)[-1] != 'Z':
            rounds += 1
        answer = (answer*rounds)//gcd(answer, rounds) # LCM
    print(answer)


filename = "input.txt"
cmd, dic = parse(filename)
# part1(cmd, dic)
part2(cmd, dic)
