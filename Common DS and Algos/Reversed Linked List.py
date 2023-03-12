# Given a Linked list, reversed every K nodes and return the head of the revsersed linked list
# use new to denote the last node that has been reversed, for a new reversal, assign K to its first node
# use old to denote the next node of new, meaning it is the next node to reverse
# use tmp to memorise the next of old. You need to store this information to link all the nodes.
# after reversing each node, move new and old and tmp forward by 1
# A small trick, always assign a node to the head of the given head of the linked list
"""
Ptr Reverse(Ptr head, int K)
{
    cnt = 1
    new = head.next
    old = new.next
    while(cnt<K):
        tmp = old.next
        old.next = new
        new = old
        old = tmp
        cnt+=1
    head.next.next = old # old has moved to the first node of next K nodes
 }
"""