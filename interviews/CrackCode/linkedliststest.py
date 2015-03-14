from linkedlists import *

end = ListNode(3, None)
mid = ListNode(2, end)
dup = ListNode(1, mid)
start1 = ListNode(3, dup)
start = ListNode(2, start1)

removedups(start)

end = ListNode(3, None)
mid = ListNode(2, end)
dup = ListNode(1, mid)
start1 = ListNode(3, dup)
start = ListNode(2, start1)


nlast(start, 5)