class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def show(self):
        node = self
        while node != None:
            print node.data
            node = node.next


def removedups(node):
    node.show()
    nodes_data = {}
    nodes_data[node.data] = 1
    prev = node
    curr = node.next
    while curr != None:
        data = curr.data
        if data in nodes_data:
            prev.next = curr.next
            curr = curr.next
        else:
            nodes_data[data] = 1
            prev = curr
            curr = curr.next
    node.show()

def nlast(node, n):
    i = 0
    curr = node
    while i < n - 1:
        curr = curr.next
        if curr == None:
            print -1
        i = i + 1
    print "current"
    print curr.data
    nlastnode = node
    while curr.next != None:
        nlastnode = nlastnode.next
        curr = curr.next
    print nlastnode.data
