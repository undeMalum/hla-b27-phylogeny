# HLA-B27 Phylogeny
HLA-B27 Phylogeny is my research project where I attempt to determine whether the clade (a group of alleles that have
evolved from a common ancestor/allele) of the HLA-B27 alleles phylogenetic tree is a reasonable predictor of the 
ankylosing spondylitis occurrence. More details will be available in my research paper, which I will not link now since 
I use it at my Biology Internal Assessment in IBDP.

Therefore, to avoid violating academic integrity, here's my candidate number to prove the code I reference in my work is
actually mine.

Candidate number: kyz635

## Projects structure
- `phylo_trees`: contains the trees I created
  - `phyloxml`: trees in [phyloxml](http://www.phyloxml.org) format
  - `png` trees as png images
- `sequences`: contains all sequences - downloaded, modified, and aligned
- `src`: contains the code I used to process sequences and create trees
  - `modyfing_sequences`: code for preprocessing data: changing headings, joining sequences, making letters capital etc.
  - `phylogenetic_tree`: code for creating and displaying trees

## Tools
Check out `requirements.txt` for the libraries I used. However, the most important are `biopython` for almost all the
work and `matplotlib` for displaying trees (biopython dependency.)

## Contribute
If you would like to contribute, just fork this repository, make some changes, and open pull request.
Any contributions are welcomed!
