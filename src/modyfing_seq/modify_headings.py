import Bio
from Bio import SeqIO

from src.base_dir import EU_SEQ_FILE, EU_SEQ_HEAD_MODIFIED_FILE


def modify_headings(seq_list: list[Bio.SeqIO.SeqRecord]):
    """
    Remove sequence and allele ID from the heading.
    Leave only the allele name.
    """

    for seq in seq_list:
        seq.id = seq.id.split("|")[1]
        seq.name = seq.name.split("|")[1]

    return seq_list


def main():
    file_format = "fasta"
    eu_with_head = list(Bio.SeqIO.parse(EU_SEQ_FILE, file_format))

    eu_without_head = modify_headings(eu_with_head)

    with open(EU_SEQ_HEAD_MODIFIED_FILE, "w") as out:
        Bio.SeqIO.write(eu_without_head, out, file_format)

    print("Headings modifies")


if __name__ == "__main__":
    main()
