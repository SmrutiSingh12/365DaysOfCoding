n = int(input())


 

for i in range(n):

    case = list(input())

    stack = []

    lookup = {'(': ')', '{': '}', '[': ']', ')': 'end', '}': 'end', ']': 'end'}


 

    for br in case:

        if ((stack !=[]) and (br in '({[')) or (stack == []):

            stack.append(br)

        elif (stack !=[]) and ((br == lookup[stack[-1]]) or (lookup[stack[-1]] == 'end')):

            del stack[-1]

 

    if len(stack) == 0:

        print('YES')

    else:

        print('NO')
