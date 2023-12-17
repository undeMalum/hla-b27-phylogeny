from Bio import Phylo

from src.base_dir import PHYLO_TREE_EU


def main():
    tree = Phylo.read(PHYLO_TREE_EU, "phyloxml")
    tree.ladderize()  # Flip branches so deeper clades are displayed at top
    Phylo.draw(tree)


if __name__ == "__main__":
    main()
