#!/usr/bin/env python
# encoding: utf-8
"""
decript_pardal.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

import sys
import os
from utils import *

# Se parar de funcionar, pode ser que tenha mudado a chave.
KEY = "5655545655381688355541151683736525351505152535455336435363716816838424040414195431239696123125941259"

def options():
  arq_input, arq_path = define_input()
  output_choice, output = define_output()
  
  return (arq_input, arq_path, output_choice, output)


def decript_pardal(**kwargs):
  """
    Essa criptografia é explicada em <http://www.mentebinaria.com.br/artigos/0x18/0x18-img2005m.html>
    
    Para descrever de modo simples o algoritmo:
    String encriptada: 665547

    1. Pegam-se dois caracteres da string encriptada e os interpreta como um número hexa:
    "66" -> 0x66

    2. Pega-se o equivalente numérico de um caractere da string chave:
    "5" -> 0x35

    3. Faz-se o xor entre esses números
    0x66 ^ 0x35 = 0x53

    4. Converte o resultado para o equivalente em ASCII.
  """
  arq_input, arq_path, output_choice, output = options()
  
  strings = get_input(arq_input, arq_path)
  
  for string in strings:
    paired_string = nsplit(string, 2)
    for char, key in zip(paired_string, KEY[0:len(paired_string)-1]):
      try:
        decrypted_char = chr(int(char, 16) ^ ord(key))
      except ValueError:
        decrypted_char = char # Se der erro, não é texto criptografado
      output.write("%s" % decrypted_char)
    output.write("\n"*2)
    
  if output_choice == 2:
    output.close()
    
  return 0
