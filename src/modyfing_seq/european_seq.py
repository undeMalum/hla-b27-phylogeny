"""It's just for training. It displays the number of sequences and sequences
themselves. Here's it's for Europeans."""

import Bio
from Bio import SeqIO

from src.base_dir import SEQUENCES

with open(SEQUENCES / "european_alleles.txt") as seq_file:
    seq_object = list(Bio.SeqIO.parse(seq_file, "fasta"))
    # print(len(seq_object), seq_object[0].name, seq_object[0].id[9:16], sep="\n")
    # print(seq_object[0].seq)
    # temp = seq_object[10].name.split("|")
    # print(temp)
    l = []
    for seq in seq_object:
        temp = ":".join(seq.name.split("|")[1].split(":")[:2])
        if temp not in l:
            l.append(temp)
            print(temp)
    print(len(l))
