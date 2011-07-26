#!/usr/bin/env python
# encoding: utf-8
"""
inverte.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

import sys
import os
from utils import *

def options():
  arq_input, arq_path = define_input()
  output_choice, output = define_output()
      
  return (arq_input, arq_path, output_choice, output)


def inverte():
  arq_input, arq_path, output_choice, output = options()
  
  strings = get_input(arq_input, arq_path)
  
  for string in strings:
    if " " in string:
      for s in string.strip().split(" "):
        output.write("%s " % s[::-1])
      output.write("\n")
    else:
      output.write("%s\n" % string[::-1])
      
  if output_choice == 2:
    output.close()
    
  return 0
