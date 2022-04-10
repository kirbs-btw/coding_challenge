def list_xor(n, arrA, arrB):
    return (n in arrA and not n in arrB) or (not n in arrA and n in arrB)

"""
learned:
there is a build in xor in python 

return (n in list1) ^ (n in list2)
"""