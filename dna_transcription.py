import re

class DNA_Transcription():

    def rna(self, dna):
        txt = dna
        rna = re.sub("T", "U", txt)
        return rna