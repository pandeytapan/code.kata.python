def decorate(func):
    print("Running the passed function inside the decorator")
    func()

    def inner():
        print("The inner function")
    return inner
