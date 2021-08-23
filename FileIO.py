with open('hello.txt', 'r') as f:
    print(line := f.read())
# with expr as var ensures that expr will be "entered" nad "exited" regardless of the code block execution