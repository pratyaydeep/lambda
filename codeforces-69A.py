(lambda n:print('YNEOS'[any(map(sum,zip(*[map(int,input().split()) for i in '-'*n])))::2]))(int(input()))
