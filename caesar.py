#!/usr/bin/env python3

from optparse import OptionParser

def cesar(n, text):
    ans = ""
    n %= 26
    for i in range(0, len(text)):
        if ord(text[i]) < 65 or ord(text[i]) > 122 or (ord(text[i]) > 90 and ord(text[i]) < 97):
            ans += text[i]
            continue
        char = chr(n + ord(text[i]))
        if ord(char) > 122 or (text[i] < 'a' and ord(char) > 90):
            char = chr(ord(char) - 26)
        ans += char
    return ans

if __name__ == "__main__":
    parser = OptionParser(description="This script is used to show how Caesar's cipher works.")
    parser.add_option("-k", "--key", dest="n", help="key", metavar="INT", default=0)
    parser.add_option("-t", "--text", dest="text", help="source text", metavar="STR", default="")
    parser.add_option("-e", "--encrypt", dest="encrypt", help="encrypt text", action="store_true", default=True)
    parser.add_option("-d", "--decrypt", dest="encrypt", help="decrypt text", action="store_false")
    parser.add_option("-b", "--brute-force", dest="brute", help="brute force attack text", action="store_true", default=False)
    args, trash = parser.parse_args()
    if args.brute:
        for i in range(0, 26):
            print(cesar(i, args.text), 26 - i)
    else:
        key = int(args.n) if args.encrypt else -int(args.n)
        print(cesar(key, args.text))
