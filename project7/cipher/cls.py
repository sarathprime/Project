def greet(name):
    def hello():
       return "hello" + name +' '+ 's'
    return hello()


greet1 = greet("sarath")
print(greet1)


def calculate(func,x,y):
    return func(x,y)



