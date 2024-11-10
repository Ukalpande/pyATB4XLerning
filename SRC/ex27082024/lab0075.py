import time

def time_decoretior(func):
    def wrapper():
        start_time =time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"time take by function {end_time-start_time}")
    return wrapper()


@time_decoretior
def test_ui_1():
    print("add a function, time taken by this function ")
    time.sleep(2) #it is wait for two sec.

#test_ui_1()

