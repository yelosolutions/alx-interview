#!/usr/bin/python3
"""
0-unlock_boxes
"""


def canUnlockAll(boxes):
    """
    Determines if n locked boxes csn be unlocked,\
    each box may contain keys to other boxes
    """
    unlocked = set([0]) #keep track of unlocked boxes
    keys = set(boxes[0]) #Keep track of keys

    while keys:
        box = keys.pop()
        if box not in unlocked:
            unlocked.add(box)
            keys.update(boxes[box])
    return len(unlocked) == len(boxes)
