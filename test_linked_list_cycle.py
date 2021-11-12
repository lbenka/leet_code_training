from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pytest

# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true


@dataclass
class SinglyLinkedListNode:
    data: int
    next: Optional[SinglyLinkedListNode]


def has_cycle(head: SinglyLinkedListNode):
    counter = set()

    def process_node(head, counter):
        if id(head) in counter:
            return 1
        if  head is None or head.next is None:
            return 0
        else:
            counter.add(id(head))
            return process_node(head.next, counter)

    return process_node(head, counter)





# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next: Optional[ListNode] = None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        counter = set()

        def process_node(head, counter):
            if id(head) in counter:
                return True
            if head is None or head.next is None:
                return False
            else:
                counter.add(id(head))
                return process_node(head.next, counter)

        return process_node(head, counter)


UNLINKED = ListNode(
    1,
    next=ListNode(
        2,
        next=ListNode(3, next=ListNode(4, next=ListNode(5))),
    ),
)

def create_linked_list():
    from copy import deepcopy
    unlinked_copy = deepcopy(UNLINKED)
    first = ListNode(10)
    last = ListNode(8, next=first)
    unlinked_copy.next.next.next = last
    first.next = unlinked_copy
    return first


@pytest.mark.parametrize(
    "linked_list, output",
    [(UNLINKED, False), (create_linked_list(), True)],
)
def test_cycles_leet(linked_list, output):
    assert Solution().hasCycle(linked_list) == output
