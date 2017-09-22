'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Note the carry
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def addTwoNumbers(l1, l2):
    cur1 = l1
    cur2 = l2
    carry = 0
    head = ListNode(-1)
    cur = head

    while None != cur1 and None != cur2:
        plus = cur1.val + cur2.val + carry
        digit = plus % 10
        carry = plus / 10
        cur.next = ListNode(digit)
        cur = cur.next
        cur1 = cur1.next
        cur2 = cur2.next
    if None != cur1:
        while None != cur1:
            plus = cur1.val + carry
            digit = plus % 10
            carry = plus / 10
            cur.next = ListNode(digit)
            cur = cur.next
            cur1 = cur1.next
    elif None != cur2:
        while None != cur2:
            plus = cur2.val + carry
            digit = plus % 10
            carry = plus / 10
            cur.next = ListNode(digit)
            cur = cur.next
            cur2 = cur2.next
    if None == cur1 and None == cur2:
        if 1 == carry:
            cur.next = ListNode(1)

    return head.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
r = addTwoNumbers(l1,l2)
print r.val
print r.next.val
print r.next.next.val