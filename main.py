#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to /output/entry.txt.
The rant: a self-checkout machine detains a shopper over a bag of rice.
"""

import os

TEXT = (
    "Unexpected item in the bagging area. It's a bag of rice. I scanned it. "
    "You watched me scan it. Now a human has been summoned to stare at the screen, "
    "press one button, and walk away like a surgeon who just saved a life. "
    "I have been detained by a robot for buying rice."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
