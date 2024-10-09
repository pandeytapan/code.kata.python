from registration_alone import register
# Lets now decorate two functions


@register
def f1():
    print("Running f1")


@register
def f2():
    print("Running f2")


def f3():
    print("Running f3")

if __name__ == '__main__':
    f1()
    f2()
    f3()
