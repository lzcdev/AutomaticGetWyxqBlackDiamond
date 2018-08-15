#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import random
import string
 

def writeToFile():
    username = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'],5))
    password = random.randint(10000,99999)
    txt= str(username) + "," + str(password) + "\n"
    with open('test.txt', 'a+') as f:
        f.write(txt)
    readFile()

def readFile():
    with open('test.txt', 'r') as f:
        print(f.read())

writeToFile()







