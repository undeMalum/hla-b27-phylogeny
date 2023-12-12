import Bio
from Bio import SeqIO

from src.base_dir import SEQ_FILE

with open(SEQ_FILE) as seq_file:
    seq_object = Bio.SeqIO.parse(seq_file, "fasta")
    # print(seq_object)
    repeated = []
    for seq in seq_object:
        if seq.id == repeated:
            pass
        # c = str(seq.id[9:16])
        if seq.id[9:16] not in repeated:
            repeated.append(seq)

    print(repeated, len(repeated), sep="\n")
