site = {
    'Home': {
        'About': {},
        'Products': {
            'Electronics': {},
            'Books': {}
        },
        'Contact': {}
    }
}

def find_page(tree, target, path=None):
    if path is None:
        path = []
    for page, subpages in tree.items():
        current_path = path + [page]
        if page == target:
            return current_path
        result = find_page(subpages, target, current_path)
        if result:
            return result
    return None

result_path = find_page(site, 'Books')
print(" -> ".join(result_path) if result_path else "Page not found")
