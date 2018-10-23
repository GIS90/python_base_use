# -*- coding: utf-8 -*-


import argparse

# parser = argparse.ArgumentParser("use of demo")
# parser.add_argument("-square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square ** 2
# if args.verbosity == 2:
#     print "the square of {} equals {}".format(args.square, answer)
# elif args.verbosity == 1:
#     print "{}^2 == {}".format(args.square, answer)
# else:
#     print answer
#
# parser = argparse.ArgumentParser("get the work mode for the data collection")
# parser.add_argument("-m", "--mode", default="file", help="you must specify which to monitor, dir or file?")
# parser.add_argument("-e", "--escape", default=False)
# args = parser.parse_args()
# print args.mode

parse = argparse.ArgumentParser('test pars')
parse.add_argument('-f', '--frist', type=str, default="file", choices=['file', 'dir'],
                   help="you must specify which to monitor, dir or file?")
parse.add_argument('-s', '--secord', type=int, default=1, choices=[0, 1, 2],
                   help='secord paras ')
args = parse.parse_args()
if args.frist:
    print args.frist
if args.secord:
    print args.secord
