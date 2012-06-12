#!/usr/bin/env python
# encoding: utf-8

from functions import *
from IOHandler import *

def functionHandler(function_name):
  arq_input, arq_path, output_choice, output = options()
  result = eval(function_name + "." + function_name + "(" + ", ".join([str(arq_input), str(arq_path)]) + ")")
  
  output.write(result)
  
  if output_choice == 2:
    output.close()
