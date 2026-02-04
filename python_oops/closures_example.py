def fun1(a):
    def handleResponse():
        print(a)  
    return handleResponse 

s = "Hello, Closure!"
closure_func1 = fun1(s)
closure_func1()

s = "Hello Python"
closure_func2 = fun1(s)
closure_func2()

s = "Manju"
closure_func3 = fun1(s)
closure_func3()