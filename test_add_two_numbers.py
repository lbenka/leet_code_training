from typing import List, Optional
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def make_num(l: ListNode, depth: int = 0):
    result = 0

    if l.next:
        result += make_num(l.next, depth + 1)
    else:
        return l.val * 10 ** depth

    return result + (l.val * 10 ** depth)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def make_list_node(num: List[str]):
            if not num:
                return
            ln = ListNode(val=int(num.pop()))
            ln.next = make_list_node(num)
            return ln

        r = make_num(l1) + make_num(l2)
        new_r = make_list_node(num=[n for n in str(r)])
        return new_r


@pytest.mark.parametrize(
    "l1, l2, output",
    [
        (
            ListNode(2, next=ListNode(4, next=ListNode(3))),
            ListNode(5, next=ListNode(6, next=ListNode(4))),
            ListNode(7, next=ListNode(0, next=ListNode(8))),
        ),
    ],
)
def test_solution(l1, l2, output):
    assert make_num(Solution().addTwoNumbers(l1, l2)) == make_num(output)
