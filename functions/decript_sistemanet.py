#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Fernando Cezar on 2011-04-14.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

from lib.IOHandler import *
from string import lowercase as letters

def decript_sistemanet(arq_input, arq_path):
  # Montando dicionário com as letras e sua posição correspondente no alfabeto
  dictionary = {}
  for letter, i in zip(letters, range(1, len(letters)+1)):
    dictionary.update({letter: i%16})
  dictionary["z"] = 0
  
  lines = read_input(arq_input, arq_path)
  
  while not lines[0].startswith("["):
    lines.pop(0)
    
  if not lines[-1].startswith("["):
    lines.pop(-1)
  
  output = ""
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
      
    output += ("%s=%s=%s\n" % (line_parts[0], clear_text, line_parts[2]))
  output += "\n"
      
  return output
