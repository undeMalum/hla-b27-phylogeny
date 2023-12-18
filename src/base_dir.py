import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.joinpath("sequences")

# European seq
EU_SEQ_FILE = BASE_DIR.joinpath("european_alleles.txt")
EU_SEQ_HEAD_MODIFIED_FILE = BASE_DIR.joinpath("european_alleles_head.txt")

# Asian seq
ASIAN_SEQ_FILE = BASE_DIR.joinpath("asian_alleles.txt")

# Joined seq
JOINED_SEQ_FILE = BASE_DIR.joinpath("joined_alleles.txt")
JOINED_SEQ_HEAD_MODIFIED_FILE = BASE_DIR.joinpath("joined_alleles_head.txt")

# Alignment
ALIGNED_EU_FILE = BASE_DIR.joinpath("aligned_european_alleles.txt")
ALIGNED_EU_FILE_HEAD = BASE_DIR.joinpath("european_alleles_head_aligned.txt")

# Phylogenetic tree
PHYLO_TREE_EU = BASE_DIR.joinpath("phylo_tree_eu.xml")
PHYLO_TREE_EU_HEAD = BASE_DIR.joinpath("phylo_tree_eu_head.xml")

if __name__ == "__main__":
    print(BASE_DIR,
          EU_SEQ_FILE,
          ASIAN_SEQ_FILE,
          JOINED_SEQ_FILE,
          ALIGNED_EU_FILE,
          PHYLO_TREE_EU,
          sep="\n"
          )
