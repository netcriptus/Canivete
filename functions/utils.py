#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Created by Fernando Cezar on 2011-07-26.
Copyright (c) 2011 8Bits Web. All rights reserved.

Este arquivo contem funções genéricas, que são usados por vários scripts
"""

def nsplit(string, group_size):
  """
    Função separa uma strings em grupos de tamanho <group_size>
  """
  return [string[k:k+group_size] for k in range(0, len(string), group_size)]
