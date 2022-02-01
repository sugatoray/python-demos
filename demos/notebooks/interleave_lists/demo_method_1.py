# Interleave multiple lists of different lengths in Python
import itertools
from typing import List, Optional, Iterable, Union

def interleave(lists: Union[List[Iterable], Iterable], *, 
               fillvalue: Optional[object]=None, 
               nofill: bool=True) -> List:
    """Interleaves multiple iterators and returns a ``list``."""
    result = []
    for batch in itertools.zip_longest(*lists, fillvalue=fillvalue):
        if nofill:
            result.extend(list(x for x in batch if x is not fillvalue))
        else:
            result.extend(list(batch))
    return result
  
# define three lists of different lengths
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = [8, 9, 10, 11, 12]

# expected output
out = [1, 4, 8, 2, 5, 9, 3, 6, 10, 7, 11, 12]

assert out == interleave([a, b, c])
