class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

# three cases fit bewteen new max or new min and we need to get curr pointing to the right area i.e just before it
        curr = head
        while curr:
            if curr.val <= insertVal <= curr.next.val:
                break
            if curr.val > curr.next.val: # end of the list/we are about to cirle
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break
            curr = curr.next
            if curr == head:
                break

        stuff = Node(insertVal)
        stuff.next = curr.next
        curr.next = stuff
        return head