

class sequence():
    """
    sequence functions
    """
    def __init__(self, seq, type):
        self.seq = seq
        self.type = type

    def complementary(self):
        """
        Convert sequence to complementary sequence
        """
        nucleo = {"A":"T", "G":"C", "C","G", "T","A"}

        comseq = []
        for nu in self.seq:
            comseq.append(nucleo[nu])
        
        return comseq

    def dna2rna(self):
        """
        Convert DNA to RNA
        """
        res = []
        for nu in self.seq:
            if nu == "T":
                nu = "U"
            res.append(nu)

        return res

    def rna2dna(self):
        """
        Convert RNA to DNA
        """
        res = []
        for nu in self.seq:
            if nu == "U":
                nu = "T"
            res.append(nu)

        return res