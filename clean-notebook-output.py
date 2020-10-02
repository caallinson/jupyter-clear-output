import json
import sys
import pytest

def main():
    if len(sys.argv) == 1:
        print('\tError: Provide Jupyter notebook to clean in command line')
        return 0
    fName = sys.argv[1]
    try:
        fRead = open(fName)
    except OSError as err:
        print("\tError in reading file")
        print(err)


if __name__ == "__main__":
    main()
