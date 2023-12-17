"""Put the Asian and European HLA-B27 alleles in one file."""

from pathlib import Path
import os

import Bio
from Bio import SeqIO

from src.base_dir import ASIAN_SEQ_FILE, EU_SEQ_FILE, JOINED_SEQ_FILE


def join_allele_regions(out_dir: Path, file_format: str):
    with open(out_dir, "w") as joined_seq, open(ASIAN_SEQ_FILE, "r") as asian_seq_it,\
            open(EU_SEQ_FILE, "r") as eu_seq_it:
        asian_seq_list = list(Bio.SeqIO.parse(asian_seq_it, file_format))
        eu_seq_list = list(Bio.SeqIO.parse(eu_seq_it, file_format))
        joined_seq_list = asian_seq_list + eu_seq_list

        Bio.SeqIO.write(joined_seq_list, joined_seq, file_format)


def main():
    chosen_file_format = "fasta"

    if not os.stat(JOINED_SEQ_FILE).st_size:
        join_allele_regions(JOINED_SEQ_FILE, chosen_file_format)
    else:
        with open(JOINED_SEQ_FILE) as join_seq:
            alleles_number = list(Bio.SeqIO.parse(join_seq, "fasta"))
            print(f"Number of alleles: {len(alleles_number)}")
            print(f"Alleles: {alleles_number}")


if __name__ == "__main__":
    main()
