# Problem: Merge Two Sorted Lists (LeetCode #21)
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Complexity: Time O(n + m), Space O(1)
# Strategy: Using a Dummy Node to simplify edge cases, iterating through both lists and pointing to the smaller node.

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2