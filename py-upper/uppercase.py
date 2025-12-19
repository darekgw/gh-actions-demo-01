#!/usr/bin/env python3

def to_uppercase(text: str) -> str:
    return text.upper()

def to_uppercase2(text: str) -> str:
    return text.tolower()
    lenght = len(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(to_uppercase(sys.argv[1]))
    else:
        print("USAGE: uppercase.p <string_to_convert>")
