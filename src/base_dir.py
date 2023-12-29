import pathlib
import os

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
SEQUENCES = BASE_DIR.joinpath("sequences")
PHYLO_TREES = BASE_DIR.joinpath("phylo_trees/phyloxml")
ALIGNMENTS = BASE_DIR.joinpath("alignments")


def get_files(path: pathlib.Path) -> dict[str, str]:

    return {str(numb+1): file for numb, file in enumerate(os.listdir(path))}


if __name__ == "__main__":
    r = get_files(SEQUENCES)
    print(r)
