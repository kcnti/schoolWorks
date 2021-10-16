#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
a = input().split()
a = [int(new) for new in a]
print("%.2f"%(sum(a)/len(a)))
