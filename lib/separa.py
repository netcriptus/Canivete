#!/usr/bin/env python
# encoding: utf-8
"""
separa.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 8Bits Web. All rights reserved.
"""

import sys
import os
from utils import *

def options():
  arq_input, arq_path = define_input()
  output_choice, output = define_output()
      
  sys.stdout.write("\n\nEm grupos de quantos devo separar a string?\n> ")
  groups_size = int(sys.stdin.readline().strip())
      
  return (arq_input, arq_path, output_choice, output, groups_size)


def separa(**kwargs):
  arq_input, arq_path, output_choice, output, groups_size = options()
  
  strings = get_input(arq_input, arq_path)
  
  for string in strings:
    start = 0
    ending = groups_size
    while start < len(string.strip()):
      output.write("%s, " % string.strip()[start:ending])
      start += groups_size
      ending += groups_size
    output.write("\n")
  if output_choice == 2:
    output.close()
  return 0
