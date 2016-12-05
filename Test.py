from sys import argv
wc = len("|This is a python script running: {}|".format(argv[0]))
spacer = "-" * wc
print spacer
print "|This is a python script running: {}|".format(argv[0])
print spacer
