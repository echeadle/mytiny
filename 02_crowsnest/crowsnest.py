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
        description='Print out what is off the larboard side',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main Program"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
