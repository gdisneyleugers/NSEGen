from sys import argv
from scapy.all import *
print "---------------------"
print "Scapy Works!"
print "Testing: {0}:{1}".format(argv[1],argv[2])
print "---------------------"
a = IP(dst=str(argv[1]))/TCP(dport=int(argv[2]))
r = send(a)
print repr(a)
print "---------------------"
