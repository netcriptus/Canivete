#!/usr/bin/env python
# encoding: utf-8
"""
canivete.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 VidaNerd.com. All rights reserved.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

def main(argv):
  opt = None
  while opt != 0:
    sys.stdout.write("\n\n0. Sair\n")
    for function, i in zip(functions, range(len(functions))):
      sys.stdout.write("%d. %s\n" %(i+1, function["desc"]))
    opt = int(sys.stdin.readline().strip())
    
    if opt > 0 and opt in range(len(functions) + 1):
      eval(functions[opt-1]["func_call"])
  return 0


if __name__ == '__main__':
  from functions import functions
  from inverte import *
  from separa import *
  sys.exit(main(sys.argv))

