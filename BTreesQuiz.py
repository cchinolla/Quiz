class StudentInformation:
    last_name = "Chinolla"
    first_name = "Catalina"
    utep_id = "80648071"


class MultipleChoice:
    @staticmethod
    def get_problem_1_answer():
        return 1 # If you think the answer is option n, return n

    @staticmethod
    def get_problem_2_answer():
        return 1  # If you think the answer is option n, return n


class BTreeNode:
    # Constructor
    def __init__(self, keys=[], children=[], is_leaf=True, max_num_keys=5):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf
        if max_num_keys < 3:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys = 3
        if max_num_keys % 2 == 0:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys += 1
        self.max_num_keys = max_num_keys

    def is_full(self):
        return len(self.keys) >= self.max_num_keys


class BTree:
    # Constructor
    def __init__(self, max_num_keys=5):
        self.max_num_keys = max_num_keys
        self.root = BTreeNode(max_num_keys=max_num_keys)

    def search_at_depth(self, k, d, node=None):  # Quiz question 3
        if node is None:
            node = self.root

        if d is 0:
            if k in node.keys:
                return node
        if node.is_leaf:
            return None
        return self.search_at_depth(k, d-1, node.children[self.find_child(k, node)])

    def height(self, node=None):  # Quiz question 4
        if node is None:
            return -1
        if node.keys:
            return 0 if node.is_leaf else 1
        return 1 + height(node.children[0])

    def count_even(self, node=None):  # Quiz question 5
        if node is None:
            return 0
        num = 0
        for child in root.children:
            if root.key % 2 == 0:
                num += count_even(child)
        return num


def main():
    print("Test here")


if __name__=="__main__":
    main()
