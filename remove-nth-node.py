class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    #remove the nth node from the end
    slow.next = slow.next.next

    return dummy.next

#example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
new_head = removeNthFromEnd(head, n)

# output of the modified list
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next