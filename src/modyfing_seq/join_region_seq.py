"""Put the HLA-B27 alleles from two regions in one file in one file."""

from pathlib import Path

import Bio
from Bio import SeqIO

from src.base_dir import get_files, SEQUENCES
from src.modyfing_seq import modify_headings


def join_allele_regions(out_dir: Path, join_seq1: Path, join_seq2: Path, file_format: str) -> None:
    with open(out_dir, "w") as joined_seq, open(join_seq1, "r") as seq1,\
            open(join_seq2, "r") as seq2:

        # Process first region sequences
        seq_list_1 = list(Bio.SeqIO.parse(seq1, file_format))
        seq_list_modified_header1 = modify_headings.modify_headings(seq_list_1, "A")

        # Process second region sequences
        seq_list2 = list(Bio.SeqIO.parse(seq2, file_format))
        seq_list_modified_header2 = modify_headings.modify_headings(seq_list2, "E")

        # Join together the list of the two region sequences
        joined_seq_list = seq_list_modified_header2 + seq_list_modified_header1

        Bio.SeqIO.write(joined_seq_list, joined_seq, file_format)


def main() -> None:
    files = get_files(SEQUENCES)
    for numb, file in files.items():
        print(f"{numb}: {file}")
    seq1 = input("""
Which sequences do you want to join?
(sequence 1)> """)
    seq2 = input("(sequence 2)> ")
    join_seq = input("""
Which file do you want to use?
> """)

    # TODO: Find a better way to ensure that the user chose different files
    if seq1 != seq2 or seq1 != join_seq or seq2 != join_seq:
        print("You chose a file multiple times.")
        return

    chosen_file_format = "fasta"
    try:
        join_allele_regions(
            SEQUENCES / files[join_seq],
            SEQUENCES / files[seq1],
            SEQUENCES / files[seq2],
            chosen_file_format
        )
    except KeyError:
        print("Wrong key.")
    else:
        print("Files were successfully joined.")

    with open(SEQUENCES / files[join_seq]) as join_seq_open:
        alleles_number = list(Bio.SeqIO.parse(join_seq_open, chosen_file_format))
        print(f"Number of alleles: {len(alleles_number)}")
        print(f"Alleles: {alleles_number}")


if __name__ == "__main__":
    main()
