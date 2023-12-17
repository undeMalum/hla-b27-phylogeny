from Bio import Phylo
import matplotlib
import matplotlib.pyplot as plt

from src.base_dir import PHYLO_TREE_EU


def display_tree():
    tree = Phylo.read(PHYLO_TREE_EU, "phyloxml")
    tree.ladderize()  # Flip branches so deeper clades are displayed at top
    Phylo.draw(tree)


def main():
    # dict_of_available_extensions = {
    #     "1": "newick",
    #     "2": "nexus",
    #     "3": "nexml",
    #     "4": "xml",
    #     "5": "cdao"
    # }
    # print(dict_of_available_extensions)
    # extension = input("Provide file extension: ")
    display_tree()
    print("Tree displayed successfully.")


if __name__ == "__main__":
    main()
