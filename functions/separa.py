#!/usr/bin/env python
# encoding: utf-8
"""
separa.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 8Bits Web. All rights reserved.
"""
import sys
from lib.IOHandler import read_input
from utils import nsplit

      
def separa(arq_input, arq_path):
  """
    Dada uma string, esse programa o separa em grupos de tamanho <group_size>
  """
  sys.stdout.write("\n\nEm grupos de quantos devo separar a string?\n> ")
  groups_size = int(sys.stdin.readline().strip())
    
  strings = read_input(arq_input, arq_path)
  output = ""
  for string in strings:
    splited_string = nsplit(string, groups_size)
    for group in splited_string:
      output += ("%s, " % group)
    output += "\n"
  
  return output
