from pathlib import Path

from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo.Consensus import bootstrap_consensus, majority_consensus
from Bio.Phylo.BaseTree import Tree
from Bio import AlignIO, Phylo

from src.base_dir import get_files, ALIGNMENTS, PHYLO_TREES


def remove_nodes_name_and_save_tree(tree: Tree, file: Path) -> None:
    for node in tree.get_nonterminals():
        node.name = None

    with open(file, "w") as phylo_tree_eu:
        Phylo.write([tree], phylo_tree_eu, "phyloxml")


def tree_construction(seq_aln: AlignIO.MultipleSeqAlignment, file_tree: Path) -> None:
    calc = DistanceCalculator("identity")
    dm = calc.get_distance(seq_aln)

    constructor = DistanceTreeConstructor()
    phylo_tree = constructor.upgma(dm)

    remove_nodes_name_and_save_tree(phylo_tree, file_tree)


def tree_construction_bootstrap(dist_calc: str, seq_aln: AlignIO.MultipleSeqAlignment, file_tree: Path) -> None:
    calculator = DistanceCalculator(dist_calc)
    constructor = DistanceTreeConstructor(calculator)

    consensus_tree = bootstrap_consensus(seq_aln, 100, constructor, majority_consensus)

    remove_nodes_name_and_save_tree(consensus_tree, file_tree)


def main() -> None:
    files = get_files(ALIGNMENTS)
    for numb, file in files.items():
        print(f"{numb}: {file}")

    seq_choice = input("""
Which sequence would you like to use?
> """)
    tree_file = input("""
Give the name for the file in which the
tree will be saved
> """) + ".xml"

    if Path(tree_file).suffix != ".xml":
        print("Don't provide file extension.")
        return

    boostrap = input("""
Do you wish to calculate bootstrap values (n/y)?
> """).lower()

    try:
        seq_aln = AlignIO.read(ALIGNMENTS / files[seq_choice], "fasta")
        if boostrap == "y":
            dist_calc_dict = {
                "1": "identity",
                "2": "blosum62",
            }
            dist_calc = input("""
Which parameter do you want to use?
1: identity
2: blosum62
> """)
            tree_construction_bootstrap(
                dist_calc_dict[dist_calc],
                seq_aln,
                PHYLO_TREES / tree_file
            )
        elif boostrap == "n":
            tree_construction(seq_aln, PHYLO_TREES / tree_file)
        else:
            print("Incorrect answer for bootstrap.")
    except KeyError:
        print("Wrong key.")
    else:
        print("Tree has been constructed successfully!")


if __name__ == "__main__":
    main()
