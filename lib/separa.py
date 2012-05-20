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
  """
    Dada uma string, esse programa o separa em grupos de tamanho <group_size>
  """
  arq_input, arq_path, output_choice, output, groups_size = options()
  
  strings = get_input(arq_input, arq_path)
  
  for string in strings:
    splited_string = nsplit(string, groups_size)
    for group in splited_string:
      output.write("%s, " % group)
    output.write("\n")
  if output_choice == 2:
    output.close()
  return 0
