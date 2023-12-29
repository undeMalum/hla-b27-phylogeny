from pathlib import Path

import Bio
from Bio import SeqIO

from src.base_dir import get_files, SEQUENCES


def modify_headings(seq_list: list[Bio.SeqIO.SeqRecord], add: str = "") -> list[Bio.SeqIO.SeqRecord]:
    """
    Remove sequence and allele ID from the heading.
    Leave only the allele name.

    e.g.
    HLA00220|B*27:01|299 ---> B*27:01 HLA00220|B*27:01|2991

    or (if parameter "add" is supplied)
    add = "E"
    HLA00220|B*27:01|299 ---> B*27:01E HLA00220|B*27:01|2991
    """

    for seq in seq_list:
        seq.id = seq.id.split("|")[1] + add
        seq.name = seq.name.split("|")[1] + add

    return seq_list


def main() -> None:
    files = get_files(SEQUENCES)
    for numb, file in files.items():
        print(f"{numb}: {file}")
    seq_old_head = input("""
In which sequence do you want to modify the headings?
> """)
    seq_new_head = input("""
Provide the name of the file in which you want to
store the sequence with the new headings.
> """)

    if Path(seq_new_head).suffix != ".txt":
        print("Incorrect file extension for the tree.")
        return

    file_format = "fasta"

    try:
        eu_with_head = list(Bio.SeqIO.parse(SEQUENCES / files[seq_old_head], file_format))
        eu_without_head = modify_headings(eu_with_head)
        with open(SEQUENCES / seq_new_head, "w") as out:
            Bio.SeqIO.write(eu_without_head, out, file_format)
    except KeyError:
        print("Wrong key.")
    else:
        print("Headings have been modified.")


if __name__ == "__main__":
    main()
