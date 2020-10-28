#!/usr/bin/env python3
"""
Author : r611171 <r611171@localhost>
Date   : 2020-10-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("picnic_items",
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='One or more picnic items')

    parser.add_argument('-s',
                        '--sorted',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    flag_arg = args.sorted
    picnic_stuff = args.picnic_items

    print(f'flag_arg = "{flag_arg}"')
    print(f'
     "{picnic_stuff}"')
    if len(picnic_stuff) == 1:
        print(f'equal 1: "{picnic_stuff}"')
    elif len(picnic_stuff) == 2:
         print(f'equal 2: "{picnic_stuff}"')
    else:
        print(f'more than 2: "{picnic_stuff}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
