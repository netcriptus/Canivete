#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Created by Fernando Cezar on 2011-07-26.
Copyright (c) 2011 8Bits Web. All rights reserved.

Este arquivo contem funçõe genéricas, que são usados por vários scripts
"""

import sys
import os

def get_input(arq_input, arq_path):
  """
    Define se o input será feita via entrada padrão ou arquivo.
    Caso a entrada seja do arquivo, tenta abri-lo.
  """
  if arq_input:
    try:
      fp = open(arq_path, "r")
    except IOError:
      sys.stderr.write("\nParece que o arquivo que você passou como entrada não existe. Digitou errado?\n")
      sys.exit(1)
    strings = fp.readlines()
    fp.close()
    
  else:
    sys.stdout.write("\nDigite uma string por linha. Deixe uma linha em branco para terminar.\n")
    strings = []
    line = sys.stdin.readline()
    while line != "\n":
      strings.append(line)
      line = sys.stdin.readline()
      
  return strings


def nsplit(string, group_size):
  """
    Função separa uma strings em grupos de tamanho <group_size>
  """
  return [string[k:k+group_size] for k in range(0, len(string), group_size)]


def define_input():
  arq_input = 0
  while arq_input < 1 or arq_input > 2:
    sys.stdout.write("\n\nA string está num arquivo, ou será digitada?\n")
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
    
  return arq_input, arq_path


def define_output():
  """
    Define se a saída do programa será em um arquivo ou na saída padrão.
    Caso seja escolhido um arquivo, devolve um ponteiro para o mesmo.
  """
  output_choice = 0
  while output_choice < 1 or output_choice > 2:
    sys.stdout.write("\n\nA saída deve ser escrita na tela?\n")
    sys.stdout.write("1. Sim, escreva o resultado na tela\n")
    sys.stdout.write("2. Não, quero um arquivo guardando o resultado\n> ")
    try:
      output_choice = int(sys.stdin.readline().strip())
    except ValueError:
      output_choice = 0
      
    if output_choice == 1:
      output = sys.stdout
    elif output_choice == 2:
      sys.stdout.write("\n\nDigite o nome do arquivo de saída\n> ")
      output = open(sys.stdin.readline().strip(), "w")
  return output_choice, output
