family_tree = {
    "Grandparent": ["Parent1", "Parent2"],
    "Parent1": ["Child1", "Child2"],
    "Parent2": ["Child3"],
    "Child1": ["Grandchild1"],
    "Child2": [],
    "Child3": [],
    "Grandchild1": []
}

def find_descendants(tree, person):
    descendants = []
    for child in tree.get(person, []):
        descendants.append(child)
        descendants.extend(find_descendants(tree, child))
    return descendants

print("Descendants of Grandparent:", find_descendants(family_tree, "Grandparent"))
