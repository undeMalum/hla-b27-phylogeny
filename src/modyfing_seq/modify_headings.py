import Bio
from Bio import SeqIO

from src.base_dir import EU_SEQ_FILE, EU_SEQ_HEAD_MODIFIED_FILE


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
    file_format = "fasta"
    eu_with_head = list(Bio.SeqIO.parse(EU_SEQ_FILE, file_format))

    eu_without_head = modify_headings(eu_with_head)

    with open(EU_SEQ_HEAD_MODIFIED_FILE, "w") as out:
        Bio.SeqIO.write(eu_without_head, out, file_format)

    print("Headings modifies")


if __name__ == "__main__":
    main()
