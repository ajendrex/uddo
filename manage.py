#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

cur_version = sys.version_info

if cur_version.major < 3 or (cur_version.major == 3 and cur_version.minor < 3):
  print("Este sitio no funcionará si la versión de python es menor a 3.3, por favor actualiza python.")
  exit()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uddo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
