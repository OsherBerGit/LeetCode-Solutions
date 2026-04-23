# Problem: Remove Nth Node From End of List (LeetCode #19)
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Complexity: Time O(n), Space O(1)
# Strategy: 

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
