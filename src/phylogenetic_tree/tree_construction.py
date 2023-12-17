from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO, Phylo

from src.base_dir import ALIGNED_EU_FILE, PHYLO_TREE_EU


def tree_construction():
    seq_aln = AlignIO.read(ALIGNED_EU_FILE, "fasta")

    calc = DistanceCalculator("identity")
    dm = calc.get_distance(seq_aln)

    constructor = DistanceTreeConstructor()
    phylo_tree = constructor.upgma(dm)

    for node in phylo_tree.get_nonterminals():
        node.name = None

    with open(PHYLO_TREE_EU, "w") as phylo_tree_eu:
        Phylo.write([phylo_tree], phylo_tree_eu, "phyloxml")


def main():
    tree_construction()


if __name__ == "__main__":
    main()
