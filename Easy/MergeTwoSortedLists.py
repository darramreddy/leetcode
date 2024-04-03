# Ekdatha Arramreddy

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoSortedLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    curr = start = ListNode()
    while list1 and list2:
        if(list1.val < list2.val):
            curr.next = list1
            curr = list1
            list1 = list1.next
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next
    if(list1):
        curr.next = list1
    elif(list2):
        curr.next = list2
    return start.next