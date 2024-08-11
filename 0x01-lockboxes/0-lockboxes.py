#!/usr/bin/python3
"""Lockboxes puzzle"""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be opened"""
    key = 1
    while key < len(boxes):
        flag = False
        box = 0
        while box < len(boxes):
            if key in boxes[box] and box != key:
                flag = True
                break
            box += 1
        if not flag:
            return False
        key += 1
    return True
