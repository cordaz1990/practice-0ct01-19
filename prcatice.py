from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    """Return the largest value in line, which is a whitespace-delimited string
    of intergers that each end with a '.'.
    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """
    #The largest value seen so far.
    largest = -1 
    for value in line .split():
      #Remove the trailing period.
      v = int(value[: -1])
      #if we find a larger value, rember it.
      if v largest:
        largest = v
        
return largest
