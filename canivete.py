#!/usr/bin/env python
# encoding: utf-8
"""
canivete.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 8Bits Web. All rights reserved.
"""

def main(functions_list):
  opt = None
  while opt != 0:
    sys.stdout.write("\n\n\t0. Sair\n")
    for function, i in zip(functions_list, range(len(functions_list))):
      sys.stdout.write("\t%d. %s\n" %(i+1, functions.descriptions[function]))
    sys.stdout.write("\n\t> ")
    try:
      opt = int(sys.stdin.readline().strip())
    except ValueError:
      opt = None
      sys.stderr.write("\n\tOpção inválida\n")
    
    if opt > 0 and opt in range(len(functions_list) + 1):
      functionHandler(functions_list[opt-1])
  return 0


if __name__ == '__main__':
  import sys
  import functions
  from lib.functionHandler import functionHandler
  
  functions_list = functions.__all__
  sys.exit(main(functions_list))

