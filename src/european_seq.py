import Bio
from Bio import SeqIO

from src.base_dir import EU_SEQ_FILE

with open(EU_SEQ_FILE) as seq_file:
    seq_object = list(Bio.SeqIO.parse(seq_file, "fasta"))
    print(len(seq_object))


