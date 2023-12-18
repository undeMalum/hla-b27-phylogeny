import Bio
from Bio import AlignIO

from src.base_dir import ALIGNED_EU_FILE_HEAD

with open(ALIGNED_EU_FILE_HEAD) as seq_file:
    seq_object = Bio.AlignIO.read(seq_file, "fasta")
    print(seq_object)

    for seq in seq_object:
        seq.seq = seq.seq.upper()

    print(seq_object)

    Bio.AlignIO.write([seq_object], ALIGNED_EU_FILE_HEAD, "fasta")
