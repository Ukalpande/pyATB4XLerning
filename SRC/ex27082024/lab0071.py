def outer_function():
    var1 = 440 #local variable

    def inner_function():
        print(var1)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()


outer_function()