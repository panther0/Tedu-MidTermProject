#!/usr/bin/env python3
#coding=utf-8
import sys
import pdb

def add(n1=0,n2=0):
    return int(n1) + int(n2)

def sub(n1=0,n2=0):
    return int(n1) - int(n2)

def main():
    print(sys.argv)

    # 开启pdb
    # pdb.set_trace()
 
    a = add(sys.argv[1],sys.argv[2])
    print(a)
    b = sub(sys.argv[1],sys.argv[2])
    print(b)

main()