#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
  
for line in sys.stdin: 
    words = re.findall(r'[a-zA-Z]+', line) 
    for word in words:
        print('%s\t%s' % (word, 1))
