import sys


def hello():
    print("Hello World")


def simple_main():
    hello()


if __name__ == '__main__':
    simple_main()


def hello_name(name="World"):
    print("Hello " + name)


def better_main():
    if len(sys.argv) > 1:
        hello_name()
