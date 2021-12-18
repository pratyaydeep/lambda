(lambda n,a:(lambda a:print(len(list(filter((lambda x:x>=a[0]/2),a)))))((list(__import__('itertools').accumulate(a,lambda x,y:x+y))[::-1])))(int(input()),sorted([int(_)for _ in input().split()]))
