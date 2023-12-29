from pathlib import Path

from Bio import Phylo

from src.base_dir import get_files, PHYLO_TREES


def display_tree(tree: Path) -> None:
    tree = Phylo.read(tree, "phyloxml")
    tree.ladderize()  # Flip branches so deeper clades are displayed at top
    Phylo.draw(tree)


def main() -> None:
    files = get_files(PHYLO_TREES)
    for numb, file in files.items():
        print(f"{numb}: {file}")
    tree = input(f"""
Which tree do you want to display?
> """)
    try:
        display_tree(PHYLO_TREES / files[tree])
    except KeyError:
        print("Wrong key.")
    else:
        print("Tree displayed successfully.")


if __name__ == "__main__":
    main()
