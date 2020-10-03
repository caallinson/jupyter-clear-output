import json
import sys  

def process_json(json_parsed):
    """
    Clear outputs from Notebook saved in JSON format
    """
    if isinstance(json_parsed, dict):
        if 'cells' in json_parsed.keys():
            for obj in json_parsed['cells']:
                if 'outputs' in obj.keys():
                    obj['outputs'] = []
        else:
            return None
    else:
        return None

    return json_parsed

def main():
    """
    Clears outputs from Notebook. Print errors and help messages as needed
    """
    if len(sys.argv) == 1:
        print('\t')
        print('\tClean Output of Jupyter Notebook Files (note: must be in JSON format)')
        print('\t')
        print('\t\t-f : Force read of non-ipynb file')
        print('\t')
        print('\t---------------------------------')
        print('\tError: Provide Jupyter notebook file path')
        print('\t')
        return 1

    fName = None
    for arg in sys.argv[1:]:
        if arg[0] != '-':
            fName = arg
    if fName is None:
        print('\tError: File name not provided')
        return 1

    if fName.lower()[-6:] != ".ipynb":
        if '-f' not in sys.argv:
            print('\tError: File not .ipynb extension')
            print('\t\tUse -f to force')
            return 1

    try:
        fRead = open(fName)
    except Exception as err:
        print("\tError in reading file")
        print(err)
        return 1

    try:
        f_contents = json.load(fRead)
    except Exception as err:
        print("\tError Parsing JSON")
        print(err)
        return 1

    fRead.close()
    f_contents = process_json(f_contents)

    if f_contents is not None:
        fWrite = open(fName, 'w')
        json.dump(f_contents, fWrite, indent=1)
    else:
        print("\tError: Couldn't process JSON")
        return 1

    return 0

if __name__ == "__main__":
    main()
