#!/usr/bin/env python
# encoding: utf-8
"""
inverte.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 8Bits Web. All rights reserved.
"""
from lib.IOHandler import read_input

def inverte(arq_input, arq_path):
  """
    Essa função inverte uma string palavra por palavra
  """
  
  strings = read_input(arq_input, arq_path)
  output = ""
  for string in strings:
    if " " in string.strip():
      for s in string.strip().split(" "):
        output += "%s" % s[::-1]
      output += "\n"
    else:
      output += "%s\n" % string[::-1]
      
  return output
