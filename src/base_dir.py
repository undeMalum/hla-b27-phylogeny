import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
SEQUENCES = BASE_DIR.joinpath("sequences")
PHYLO_TREES = BASE_DIR.joinpath("phylo_trees/phyloxml")

# European seq
EU_SEQ_FILE = SEQUENCES.joinpath("european_alleles.txt")
EU_SEQ_HEAD_MODIFIED_FILE = SEQUENCES.joinpath("european_alleles_head.txt")

# Asian seq
ASIAN_SEQ_FILE = SEQUENCES.joinpath("asian_alleles.txt")

# Joined seq
JOINED_SEQ_FILE = SEQUENCES.joinpath("joined_alleles.txt")
JOINED_SEQ_HEAD_MODIFIED_FILE = SEQUENCES.joinpath("joined_alleles_head.txt")

# Alignment
ALIGNED_EU_FILE = SEQUENCES.joinpath("aligned_european_alleles.txt")
ALIGNED_EU_FILE_HEAD = SEQUENCES.joinpath("european_alleles_head_aligned.txt")
ALIGNED_JOINED_SEQ_HEAD_MODIFIED_FILE = SEQUENCES.joinpath("joined_alleles_head_alignment.txt")

# Phylogenetic tree
PHYLO_JOINED_NO_BOOTSTRAP = PHYLO_TREES.joinpath("joined_alleles_head_no_boostrap.xml")
PHYLO_TREE_EU_HEAD_BLOSUM = PHYLO_TREES.joinpath("phylo_tree_eu_head_blosum62.xml")
PHYLO_TREE_EU_HEAD_IDENTITY = PHYLO_TREES.joinpath("phylo_tree_eu_head_identity.xml")
PHYLO_TREE_EU_HEAD_NO_BOOTSTRAP = PHYLO_TREES.joinpath("phylo_tree_eu_head_no_boostrap.xml")

if __name__ == "__main__":
    print(BASE_DIR,
          EU_SEQ_FILE,
          ASIAN_SEQ_FILE,
          JOINED_SEQ_FILE,
          ALIGNED_EU_FILE,
          sep="\n"
          )
