import plistlib
import argparse



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--plist-path',action="store",default=None, help='Specify the path of the plist to read',required=False)
    parser.add_argument('--key-to-extract',action="store",default=None, help='Specify the key to extract from the plist',required=False)

    args = parser.parse_args()


    with open(args.plist_path, 'rb') as f:
        plist_file = plistlib.load(f)

    for value in plist_file:
        print (value[args.key_to_extract])