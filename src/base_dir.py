import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
SEQ_FILE = BASE_DIR.joinpath("alleles.txt")


if __name__ == "__main__":
    print(BASE_DIR, SEQ_FILE, sep="\n")
