from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo.Consensus import bootstrap_consensus, bootstrap, bootstrap_trees, majority_consensus
from Bio import AlignIO, Phylo

from src.base_dir import ALIGNED_EU_FILE_HEAD, PHYLO_TREE_EU_HEAD


def tree_construction():
    seq_aln = AlignIO.read(ALIGNED_EU_FILE_HEAD, "fasta")

    calc = DistanceCalculator("identity")
    dm = calc.get_distance(seq_aln)

    constructor = DistanceTreeConstructor()
    phylo_tree = constructor.upgma(dm)

    for node in phylo_tree.get_nonterminals():
        node.name = None

    with open(PHYLO_TREE_EU_HEAD, "w") as phylo_tree_eu:
        Phylo.write([phylo_tree], phylo_tree_eu, "phyloxml")


def tree_construction_bootstrap():
    seq_aln = AlignIO.read(ALIGNED_EU_FILE_HEAD, "fasta")
    msas = bootstrap(seq_aln, 100)

    calculator = DistanceCalculator("identity")
    constructor = DistanceTreeConstructor(calculator)
    trees = next(bootstrap_trees(seq_aln, 100, constructor))

    consensus_tree = bootstrap_consensus(seq_aln, 100, constructor, majority_consensus)

    for node in trees.get_nonterminals():
        node.name = None

    with open(PHYLO_TREE_EU_HEAD, "w") as phylo_tree_eu:
        Phylo.write([trees], phylo_tree_eu, "phyloxml")


def main():
    tree_construction()


if __name__ == "__main__":
    main()
