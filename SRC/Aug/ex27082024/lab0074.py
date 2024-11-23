#with out wraper you can use like below
#but in this case modify the test case
# fi you dont want to crate new function then you can use decoretor

def start():
    print("Before runing  Ui tc")
    print("starting the browser")


def end():
    print("end the runing Ui tc")
    print("quite Browser")

def test_ui():
    print("i will test UI")


start()
end()
test_ui()