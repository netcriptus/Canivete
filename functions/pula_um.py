#!/usr/bin/env python
# encoding: utf-8
"""
pula-um.py

Created by Fernando Cezar on 2012-05-20.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from lib.IOHandler import *

def pula_um(arq_input, arq_path):
  """
    Dado uma string, lê um caracter sim e um não.
  """
  strings = read_input(arq_input, arq_path)
  decrypted_string = ""
  for string in strings:
    decrypted_string += string[::2] + "\n"
  return decrypted_string
