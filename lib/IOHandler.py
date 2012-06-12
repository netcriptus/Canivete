#!/usr/bin/env python
# encoding: utf-8

import sys
from messages import notice, error

def options():
  arq_input, arq_path = define_input()
  output_choice, output = define_output()
  return (arq_input, arq_path, output_choice, output)


def read_input(arq_input, arq_path):
  if arq_input:
    try:
      fp = open(arq_path, "r")
    except IOError:
      sys.stderr.write(error["file missing"])
      sys.exit(1)
    strings = fp.readlines()
    fp.close()
  
  else:
    sys.stdout.write(notice["input instructions"])
    strings = []
    line = sys.stdin.readline()
    while line != "\n":
      strings.append(line)
      line = sys.stdin.readline()
  
  return strings


def define_input():
  arq_input = 0
  while arq_input < 1 or arq_input > 2:
    sys.stdout.write(notice["input location"])
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
    sys.stdout.write(notice["output location"])
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
