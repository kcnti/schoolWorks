import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
sentences = str(input())
a = ' '.join(reversed(sentences.split(' ')))
x = a.swapcase()
print(x)



#if __name__ == '__main__':