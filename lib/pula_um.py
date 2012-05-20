#!/usr/bin/env python
# encoding: utf-8
"""
pula-um.py

Created by Fernando Cezar on 2012-05-20.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from utils import *

def options():
  arq_input, arq_path = define_input()
  output_choice, output = define_output()
  
  return (arq_input, arq_path, output_choice, output)


def pula_um(**kwargs):
  """
    Dado uma string, lê um caracter sim e um não.
  """
  arq_input, arq_path, output_choice, output = options()
  
  strings = get_input(arq_input, arq_path)
  
  for string in strings:
    decrypted_string = string[::2]
    output.write("%s\n" % decrypted_string)
  output.write("\n")
    
  if output_choice == 2:
    output.close()
    
  return 0