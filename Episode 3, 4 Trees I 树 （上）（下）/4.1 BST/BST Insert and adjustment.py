# adjusting BST
# Right Right Rotate (signle left rotation)
# The new node inserted is on the right of right of the root node
# i.e A->b->c from right, insert D on either left or right child of C
# in this case, 1. make B the new root 2. detach the left child of B to a

# Left Left Rotate (signle left rotation)
# The new node inserted is on the left of left of the root node
# i.e A->b->c from left, insert D on either left or right child of c
# in this case, 1. detach b and A 2. link c and A to make c the left child of A
# 3. attach b to c again as right child.

# Left Right Rotate, 
# The new node inserted is on the right child of left child of the root node
# i.e. A->b->c from left to right, insert D on either left or right child of C
# The key is to rebalance A->b->c, not the rest of the tree
# The new root node should be the mid of a,b,c, which is b
# in this case, 1. put C as the new root node. Link a to the right of C
# 2. link b to C as the left child  3. link the inserted node d to right of b because d
# was inserted initially to c, on the right of b, meaning it is larger than b

# Right Left Rotation
# The new node inserted is on the left child of right child of the root node
# i.e. A->b->c from right to left, insert D on either left or right child of C
# The new root node should be the mid of a,b,c, which is c in this case
# in this case A should be on c's left as it is smaller, B should be on c's right as it is larger
# 1. detach a from it's parent and make C the root of this sub tree
# 2. link a to the left of C. 3. given C is smaller than b, whatever children of C can be attached to
# the left of b. Link b to the right of C



