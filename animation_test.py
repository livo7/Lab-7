import os
import time


def Cadr(x):
    if x == "q":
        print("")
    if x == "w":
        print("*")
    if x == "e":
        print("**")
    if x == "r":
        print("***")


alf = "qwer"
for _ in range(100):
    for i in alf:
        Cadr(i)
        time.sleep(0.5)
        os.system("cls")
