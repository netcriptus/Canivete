#!/usr/bin/env python
# encoding: utf-8
"""
inverte.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

import sys
import os


def main(argv):
  if len(argv) < 2:
    sys.stderr.write("E necessário passar pelo menos um número\n")
    return 1
  
  sys.stdout.write("\n")
  for num in argv[1:]:
    sys.stdout.write("%s " % num[::-1])
  sys.stdout.write("\n")


if __name__ == '__main__':
  sys.exit(main(sys.argv))

