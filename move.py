from subprocess import check_output
from random import randint
from time import sleep

def wiggle():
    print("wiggle")
    x = randint(0,500)
    y = randint(0, 500)
    print(x,y)
    cmd = ["cliclick", 'm:%s,%s' % (x,y)]
    check_output(cmd)

while True:
    wiggle()
    sleep(25)
