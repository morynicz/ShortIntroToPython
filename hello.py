import sys


def hello():
    print("Hello World")


def simple_main():
    hello()


def hello_name(name="World"):
    print("Hello " + name)


def better_main():
    if len(sys.argv) > 2:
        hello_name(sys.argv[1])


if __name__ == '__main__':
    better_main()
