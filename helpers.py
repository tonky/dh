#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import struct

 
from random import getrandbits
g = 2
prime = 7919
bits = 32
 
# a = getrandbits(bits)
# A = pow(g, a, prime)
#  
# b = getrandbits(bits)
# B = pow(g, b, prime)
#  
# s1 = pow(A, b, prime)
# s2 = pow(B, a, prime)
#  
# if(s1 == s2):
#     print("Shared secrets match: ", s1)
