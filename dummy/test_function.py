import numpy as np

def create_random_seq(length):
    nucleotides = ["A","G","C","T"]

    res=[]
    for i in range(length):
        res.append(np.random.choice(nucleotides, size=1))

    return res


