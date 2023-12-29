"""It's just for training. It displays the number of sequences and sequences
themselves. Here's it's for Asians."""

import Bio
from Bio import SeqIO

from src.base_dir import SEQUENCES

with open(SEQUENCES / "asian_alleles.txt") as seq_file:
    seq_object = list(Bio.SeqIO.parse(seq_file, "fasta"))
    print(len(seq_object))
    for seq in seq_object:
        print(seq)
