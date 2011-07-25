#!/usr/bin/env python
# encoding: utf-8
"""
separa.py

Created by Fernando Cezar on 2011-07-25.
Copyright (c) 2011 __VidaNerd.com__. All rights reserved.
"""

import sys
import os


def main(argv):
  if len(argv) < 2:
    sys.stderr.write("E necessário passar um número\n")
    return 1
  
  for num1, num2 in zip(argv[1][::2], argv[1][1::2]):
    sys.stdout.write("%s%s, " % (num1, num2))
  sys.stdout.write("\n")


if __name__ == '__main__':
  sys.exit(main(sys.argv))

