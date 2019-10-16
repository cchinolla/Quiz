class StudentInformation:
    last_name = "Your last name goes here"
    first_name = "Your last name goes here"
    utep_id = "Your UTEP ID goes here"


class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def sum_all(self, node=None):  # Quiz Problem 1
        if node is None:
            return 0
        return node.key + sum_all(node.left)+sum_all(node.right)


    def min_at_depth(self, depth, node=None):  # Quiz Problem 2
        if node is None:
            node = self.root

        if depth > self.height(self.root):
            return None
        if depth is 0:
            return node.item

        return min(self.min_at_depth(depth-1, node.left), self.min_at_depth(depth-1, node.right))

    def count_smaller_than_k(self, depth, node=None):  # Quiz Problem 3
        if root is None:
            return 0
        if root.right is not None:
            if node.item <= k:
                return 1 + count_smaller_than_k(root.right, k)
        if root.left is not None:
            if node.item<= k:
                return 1 + count_smaller_than_k(root.left,k)
        return 0


def main():
    print("Test here")


if __name__=="__main__":
    main()
