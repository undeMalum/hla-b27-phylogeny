import Bio
from Bio import SeqIO


from src.base_dir import get_files, ALIGNMENTS


def remove_duplicate_alleles(seq_list: list[Bio.SeqIO.SeqRecord]) -> list[Bio.SeqIO.SeqRecord]:
    """
    If there are two or more sequences of the same subtype, like so:

    B*27:02:01:01 and B*27:02:01:04

    leave only the first one that appears as B*27:02.

    """
    list_headings = []
    list_sequences = []
    for seq in seq_list:
        if seq.id not in list_headings:
            list_headings.append(seq.id)
            list_sequences.append(seq)

    return list_sequences


def main() -> None:
    files = get_files(ALIGNMENTS)
    for numb, file in files.items():
        print(f"{numb}: {file}")

    aligned_seq = input("""
From which sequence do you want to remove duplicate alleles?
> """)
    file_format = "fasta"
    try:
        with_duplicates = list(Bio.SeqIO.parse(ALIGNMENTS / files[aligned_seq], file_format))
        without_duplicates = remove_duplicate_alleles(with_duplicates)
        with open(ALIGNMENTS / files[aligned_seq], "w") as out:
            Bio.SeqIO.write(without_duplicates, out, file_format)
    except KeyError:
        print("Wrong key.")
    else:
        print("Duplicates removed.")


if __name__ == "__main__":
    main()
