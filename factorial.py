# The User is supposed to enter the inputs for each function

# 1st Form 



(lambda Function,Input:
    __import__('sys').setrecursionlimit(10000000)
    or
    print(Function(Input,Function))
)(
    (lambda n,this:
        1 if n<=1 else n*this(n-1,this)
    ),
    int(input())
)

# Final Form

(lambda Function,Input,Lib:
    Lib.setrecursionlimit(10000000)
    or
    print(Function(Input,Function))
)(
    (lambda n,this:
        1 if n<=1 else n*this(n-1,this)
    ),
    int(input()),
    __import__('sys')
)

# Final Form Release
(lambda Function,Input,Lib: Lib.setrecursionlimit(10000000) or print(Function(Input,Function))) ((lambda n,this:1 if n<=1 else n*this(n-1,this)),int(input()),__import__('sys'))
