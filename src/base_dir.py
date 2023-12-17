import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.joinpath("sequences")
EU_SEQ_FILE = BASE_DIR.joinpath("european_alleles.txt")
ASIAN_SEQ_FILE = BASE_DIR.joinpath("asian_alleles.txt")
JOINED_SEQ_FILE = BASE_DIR.joinpath("joined_alleles.txt")
ALIGNED_EU_FILE = BASE_DIR.joinpath("aligned_european_alleles.txt")
PHYLO_TREE_EU = BASE_DIR.joinpath("phylo_tree_eu.xml")

if __name__ == "__main__":
    print(BASE_DIR,
          EU_SEQ_FILE,
          ASIAN_SEQ_FILE,
          JOINED_SEQ_FILE,
          ALIGNED_EU_FILE,
          PHYLO_TREE_EU,
          sep="\n"
          )
