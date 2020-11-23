import pytest
from dna_transcription import DNA_Transcription

def test_dna_transcription():
    dt = DNA_Transcription()
    assert dt.rna("TTT") == "UUU"
    assert dt.rna("CCAGGACCAGGCCCCAGGTGGGGCCAGGCCAGGCTC") == "CCAGGACCAGGCCCCAGGUGGGGCCAGGCCAGGCUC"