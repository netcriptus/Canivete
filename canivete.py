#!/usr/bin/env python
# encoding: utf-8
"""
canivete.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 8Bits Web. All rights reserved.
"""

import sys
from lib import *

def main(argv):
  opt = None
  while opt != 0:
    sys.stdout.write("\n\n\t0. Sair\n")
    for function, i in zip(functions, range(len(functions))):
      sys.stdout.write("\t%d. %s\n" %(i+1, function["desc"]))
    sys.stdout.write("\n\t> ")
    try:
      opt = int(sys.stdin.readline().strip())
    except ValueError:
      opt = None
      sys.stderr.write("\n\tOpção inválida\n")
    
    if opt > 0 and opt in range(len(functions) + 1):
      eval(functions[opt-1]["func_call"])
  return 0


if __name__ == '__main__':
  """
    As funções devem ser incluídas aqui e na lista de funções
    (lib/functions.py), cada arquivo é uma função nova.
  """
<<<<<<< HEAD
  
  from functions import functions
  from inverte import *
  from separa import *
  from decript_pardal import *
  from pula_um import *
=======
  from lib.functions import functions
>>>>>>> ecc31bc16b97d7398426d7911b69d8259d005908
  sys.exit(main(sys.argv))

