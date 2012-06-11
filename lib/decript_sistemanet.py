#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Fernando Cezar on 2011-04-14.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

import sys
from utils import *

def options():
  arq_input, arq_path = define_input()
  output_choice, output = define_output()
  
  return (arq_input, arq_path, output_choice, output)


# Montando dicionário com as letras e sua posição correspondente no alfabeto
dictionary = {}
for i in range(97, 124):
  dictionary.update({chr(i): (i-96)%16})

dictionary["z"] = 0

def decript_sistemanet(**kwargs):
  arq_input, arq_path, output_choice, output = options()    
  
  lines = get_input(arq_input, arq_path)
  
  while not lines[0].startswith("["):
    lines.pop(0)
    
  if not lines[-1].startswith("["):
    lines.pop(-1)
    
  for line in lines:
    line_parts = line.strip()
    line_parts = line_parts.split("=")
    text = line_parts[1].replace(")", "")
    text = text.split("j")
    ascii_text = []
    for block in text:
      ascii_block = ""
      for letter, in block:
        ascii_block += str(dictionary[letter])
      if ascii_block:
        ascii_text += [int(ascii_block)]
        
    clear_text = ""
    for block in ascii_text:
      clear_text += chr(block)
      
    output.write("%s=%s=%s\n" % (line_parts[0], clear_text, line_parts[2]))
  output.write("\n")
  
  if output_choice == 2:
    output.close()
      
  return 0
