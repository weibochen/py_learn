# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('indir', type=str, help='Input dir for videos')
parser.add_argument('outdir', type=str, help='Output dir for image')
parser.add_argument('-m', '--my_optional',type = int, default = 2, help = 'provide an integer (default: 2)')

args = parser.parse_args()
print(args.indir)
print(my_namespace.my_optional)
