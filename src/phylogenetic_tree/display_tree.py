from pathlib import Path

from Bio import Phylo

from src.base_dir import (
    PHYLO_TREE_EU_HEAD_BLOSUM,
    PHYLO_TREE_EU_HEAD_IDENTITY,
    PHYLO_TREE_EU_HEAD_NO_BOOTSTRAP
)


def display_tree(tree: Path):
    tree = Phylo.read(tree, "phyloxml")
    tree.ladderize()  # Flip branches so deeper clades are displayed at top
    Phylo.draw(tree)


def main():
    trees_dict = {
        "1": PHYLO_TREE_EU_HEAD_BLOSUM,
        "2": PHYLO_TREE_EU_HEAD_IDENTITY,
        "3": PHYLO_TREE_EU_HEAD_NO_BOOTSTRAP
    }

    try:
        tree = input(f"""
    Which tree do you want to display?
    > """)
        display_tree(trees_dict[tree])
    except KeyError:
        print("Wrong key")
    else:
        print("Tree displayed successfully.")


if __name__ == "__main__":
    main()
