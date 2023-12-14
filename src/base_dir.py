import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
EU_SEQ_FILE = BASE_DIR.joinpath("european_alleles.txt")
ASIAN_SEQ_FILE = BASE_DIR.joinpath("asian_alleles.txt")
JOINED_SEQ_FILE = BASE_DIR.joinpath("joined_alleles.txt")

if __name__ == "__main__":
    print(BASE_DIR,
          EU_SEQ_FILE,
          ASIAN_SEQ_FILE,
          JOINED_SEQ_FILE,
          sep="\n"
          )
