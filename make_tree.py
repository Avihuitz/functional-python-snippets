def make_tree(value, left=None, right=None):

    def get_value(): return value
    def get_left(): return left
    def get_right(): return right
    def print_tree():
        def inorder(t):
            if t is not None:
                inorder(t("left"))
                print(t("value"), end=" ")
                inorder(t("right"))
        inorder(dispatch)

    def count_value(val):
        count = 0
        if dispatch("value") == val:
            count += 1
        count += dispatch("left")("count_value")(val) if dispatch("left") else 0
        count += dispatch("right")("count_value")(val) if dispatch("right") else 0
        return count

    def tree_BST():
        def is_BST(t, min_val, max_val):
            if t is None:
                return True
            val = t("value")
            if (min_val is not None and val <= min_val) or (max_val is not None and val >= max_val):
                return False
            return is_BST(t("left"), min_val, val) and is_BST(t("right"), val, max_val)
        return is_BST(dispatch, None, None)

    def tree_depth():
        if dispatch is None:
            return -1
        left = dispatch("left")
        right = dispatch("right")
        left_depth = left("tree_depth")() if left else -1
        right_depth = right("tree_depth")() if right else -1
        return 1 + max(left_depth, right_depth)

    def tree_balanced():
        left = dispatch("left")
        right = dispatch("right")
        left_depth = left("tree_depth")() if left else -1
        right_depth = right("tree_depth")() if right else -1
        if abs(left_depth - right_depth) > 1:
            return False
        return (left("tree_balanced")() if left else True) and (right("tree_balanced")() if right else True)

    def dispatch(msg):
        if msg == "value": return get_value()
        elif msg == "left": return get_left()
        elif msg == "right": return get_right()
        elif msg == "print_tree": return print_tree
        elif msg == "count_value": return count_value
        elif msg == "tree_depth": return tree_depth
        elif msg == "tree_BST": return tree_BST
        elif msg == "tree_balanced": return tree_balanced
        else: return 'unknown command'
    return dispatch