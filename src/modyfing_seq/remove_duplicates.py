import Bio
from Bio import SeqIO

from src.base_dir import ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE


def modify_headings(seq_list: list[Bio.SeqIO.SeqRecord]):
    """
    Remove sequence and allele ID from the heading.
    Leave only the allele name.
    """
    list_headings = []
    list_sequences = []
    for seq in seq_list:
        if seq.id not in list_headings:
            print(seq.id)
            list_headings.append(seq.id)
            list_sequences.append(seq)

    return list_sequences


def main():
    file_format = "fasta"
    eu_with_head = list(Bio.SeqIO.parse(ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE, file_format))

    print(len(eu_with_head))

    eu_without_head = modify_headings(eu_with_head)

    print(len(eu_without_head))

    # with open(EU_SEQ_HEAD_MODIFIED_FILE, "w") as out:
    #     Bio.SeqIO.write(eu_without_head, out, file_format)

    print("Headings modifies")


if __name__ == "__main__":
    main()
