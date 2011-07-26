#!/usr/bin/env python
# encoding: utf-8
"""
inverte.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

import sys
import os

def options():
  arq_input = 0
  while arq_input < 1 or arq_input > 2:
    sys.stdout.write("\n\nA string para inverter está num arquivo, ou será digitada?\n")
    sys.stdout.write("1. Eu mesmo vou digitar\n")
    sys.stdout.write("2. Estou com preguiça, leia do arquivo\n> ")
    try:
      arq_input = int(sys.stdin.readline().strip())
    except ValueError:
      pass
  if arq_input == 2:
    arq_input = True
    sys.stdout.write("\n\nDigite o caminho para o arquivo:\n> ")
    arq_path = sys.stdin.readline().strip()
  else:
    arq_input = False
    arq_path = None
    
  output_choice = 0
  while output_choice < 1 or output_choice > 2:
    sys.stdout.write("\n\nA saída deve ser escrita na tela?\n")
    sys.stdout.write("1. Sim, escreva o resultado na tela\n")
    sys.stdout.write("2. Não, quero um arquivo guardando o resultado\n> ")
    try:
      output_choice = int(sys.stdin.readline().strip())
    except ValueError:
      pass
      
    if output_choice == 1:
      output = sys.stdout
    else:
      sys.stdout.write("\n\nDigite o nome do arquivo de saída\n> ")
      output = open(sys.stdin.readline().strip(), "w")
      
  return (arq_input, arq_path, output_choice, output)


def inverte():
  arq_input, arq_path, output_choice, output = options()
  
  if arq_input:
    try:
      fp = open(arq_path, "r")
    except IOError:
      sys.stderr.write("\nParece que o arquivo que você passou como entrada não existe. Digitou errado?\n")
      return 1
    strings = fp.readlines()
    fp.close()
    
  else:
    sys.stdout.write("\nDigite uma string por linha. Deixe uma linha em branco para terminar.\n")
    strings = []
    line = sys.stdin.readline()
    while line != "\n":
      strings.append(line)
      line = sys.stdin.readline()
    
  
  for string in strings:
    output.write("%s\n" % string.strip()[::-1])
  if output_choice == 2:
    output.close()
    
  return 0
