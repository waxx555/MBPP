'''
Write a function to reflect the modified run-length encoding from a list.
'''


from itertools import groupby
def modified_encode(alist):
        def ctr_ele(el):
            if len(el)>1: return [len(el), el[0]]
            else: return el[0]
        return [ctr_ele(list(group)) for key, group in groupby(alist)]


assert modified_encode([1,1,2,3,4,4,5,1])==[[2, 1], 2, 3, [2, 4], 5, 1]
assert modified_encode('automatically')==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']
assert modified_encode('python')==['p', 'y', 't', 'h', 'o', 'n']
