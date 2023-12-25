from pathlib import Path

from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo.Consensus import bootstrap_consensus, majority_consensus
from Bio.Phylo.BaseTree import Tree
from Bio import AlignIO, Phylo

from src.base_dir import (
    ALIGNED_EU_FILE_HEAD,
    ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE,
    PHYLO_TREE_EU_HEAD_NO_BOOTSTRAP,
    PHYLO_TREE_EU_HEAD_IDENTITY,
    PHYLO_TREE_EU_HEAD_BLOSUM,
    PHYLO_JOINED_NO_BOOTSTRAP
)


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


def tree_construction_bootstrap(seq_aln: AlignIO.MultipleSeqAlignment, file_tree: Path) -> None:
    calculator = DistanceCalculator("blosum62")
    constructor = DistanceTreeConstructor(calculator)

    consensus_tree = bootstrap_consensus(seq_aln, 100, constructor, majority_consensus)

    remove_nodes_name_and_save_tree(consensus_tree, file_tree)


def main() -> None:
    trees_dict = {
        "1": PHYLO_TREE_EU_HEAD_BLOSUM,
        "2": PHYLO_TREE_EU_HEAD_IDENTITY,
        "3": PHYLO_TREE_EU_HEAD_NO_BOOTSTRAP,
        "4": PHYLO_JOINED_NO_BOOTSTRAP
    }
    seq_dict = {
        "1": ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE,
        "2": ALIGNED_EU_FILE_HEAD
    }

    seq_choice = input("""
Which sequence would you like to use?
> """)
    tree_algorithm = input("""
What kind of tree do you want to construct?
> """)
    boostrap = input("""
Do you wish to calculate bootstrap values?
> """)
    try:
        seq_aln = AlignIO.read(seq_dict[seq_choice], "fasta")
        if boostrap.lower() == "yes":
            tree_construction(seq_aln, trees_dict[tree_algorithm])
        elif boostrap.lower() == "no":
            tree_construction_bootstrap(seq_aln, trees_dict[tree_algorithm])
    except KeyError:
        print("Wrong key.")
    else:
        print("Tree constructed successfully!")


if __name__ == "__main__":
    main()
