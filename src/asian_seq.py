import Bio
from Bio import SeqIO

from src.base_dir import ASIAN_SEQ_FILE

with open(ASIAN_SEQ_FILE) as seq_file:
    seq_object = list(Bio.SeqIO.parse(seq_file, "fasta"))
    print(len(seq_object))
    for seq in seq_object:
        print(seq)
