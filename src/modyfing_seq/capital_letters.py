from pathlib import Path

import Bio
from Bio import AlignIO

from src.base_dir import ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE, ALIGNED_EU_FILE_HEAD


def make_capital_letters(aligned_seq: Path) -> None:
    with open(aligned_seq) as seq_file:
        seq_object = Bio.AlignIO.read(seq_file, "fasta")

        for seq in seq_object:
            seq.seq = seq.seq.upper()

        Bio.AlignIO.write([seq_object], aligned_seq, "fasta")


def main() -> None:
    aligned_seq_dict = {
        "1": ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE,
        "2": ALIGNED_EU_FILE_HEAD
    }
    aligned_seq = input("""
In which sequence do you want to make capital letters?
> """)
    try:
        make_capital_letters(aligned_seq_dict[aligned_seq])
    except KeyError:
        print("Wrong key.")
    else:
        print("Letters are now capital")


if __name__ == "__main__":
    main()
