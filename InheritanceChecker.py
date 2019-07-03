def fill_dynamic_array(entries_number):
    array_to_fill = []
    while len(array_to_fill) < entries_number:
        another_entry = input()
        array_to_fill.append(another_entry)
    return array_to_fill


def sort_relatives(classes_lineage):
    classes_relation = {}
    splitted_classes = []
    for custom_class in classes_lineage:
        splitted_classes.append(custom_class.split(':'))

    for item in splitted_classes:
        if len(item) > 1:
            classes_relation[item[0].strip()] = item[1].strip().split(' ')
        else:
            classes_relation[item[0].strip()] = ['None']

    return classes_relation


def check_requests(requests, classes_relation):
    splitted_requests = []
    for request in requests:
        splitted_requests.append(request.split(' '))

    for pair in splitted_requests:
        if find_ancestor(classes_relation, pair[1], pair[0], []) is not None:
            print('Yes')
        else:
            print('No')


def find_ancestor(classes_relation, start, end, path):
    path += [start]
    if start not in classes_relation.keys():
        return None

    if start == end:
        return path

    for node in classes_relation[start]:
        if node not in path:
            newpath = find_ancestor(classes_relation, node, end, path)

            if newpath:
                return newpath

    return None


classes_number = int(input())
classes_lineage = fill_dynamic_array(classes_number)
requests_number = int(input())
requests = fill_dynamic_array(requests_number)
classes_relation = sort_relatives(classes_lineage)
print(check_requests(requests, classes_relation))