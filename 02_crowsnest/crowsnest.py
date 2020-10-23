#!/usr/bin/env python3
"""
Author : Edward Cheadle <edward.cheadle8@gmail.com>
Date   : 2020-10-22
Purpose: Crows nest print a word
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str',help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    article = "a"
    args = get_args()  
    word = args.word

    print(f'Ahoy, Captain, {article} {word} off the larbord bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
