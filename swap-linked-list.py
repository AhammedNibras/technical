class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        prev.next, first.next, second.next = second, second.next, first
        prev = first

    return dummy.next

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

#example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original list:")
printList(head)

#swap every two adjacent nodes
head = swapPairs(head)

print("After swapping every two adjacent nodes:")
printList(head)