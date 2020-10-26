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
        description="Crows Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="str", help="A word")
    parser.add_argument('-s',
                        '--starboard',
                        help='Choose starboard side of ship if true',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main Program"""

    args = get_args()
    word = args.word
    side = args.starboard
    article = "an" if word[0].lower() in "aeiou" else "a"
    ship_side = 'starboard' if side else "larboard"
    if word[0].isupper():
        out_article = article.capitalize()
    else:
        out_article = article

    print(f"Ahoy, Captain, {out_article} {word} off the {ship_side} bow!")

# --------------------------------------------------
if __name__ == "__main__":
    main()
