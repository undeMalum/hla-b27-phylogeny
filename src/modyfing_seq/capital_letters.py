from pathlib import Path

import Bio
from Bio import AlignIO

from src.base_dir import get_files, ALIGNMENTS


def make_capital_letters(aligned_seq: Path) -> None:
    with open(aligned_seq) as seq_file:
        seq_object = Bio.AlignIO.read(seq_file, "fasta")

        for seq in seq_object:
            seq.seq = seq.seq.upper()

        Bio.AlignIO.write([seq_object], aligned_seq, "fasta")


def main() -> None:
    files = get_files(ALIGNMENTS)
    for numb, file in files.items():
        print(f"{numb}: {file}")
    aligned_seq = input("""
In which sequence do you want to make capital letters?
> """)
    try:
        make_capital_letters(ALIGNMENTS / files[aligned_seq])
    except KeyError:
        print("Wrong key.")
    else:
        print("Letters are now capital")


if __name__ == "__main__":
    main()
