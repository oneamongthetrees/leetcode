# reverse linked list
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    rev = None
    top = head
    while top:
        n = top.next
        top.next = rev
        rev = top
        top = n
    return rev