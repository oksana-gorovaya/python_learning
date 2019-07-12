import itertools


def fill_dynamic_array(entries_number):
    array_to_fill = []
    while len(array_to_fill) < entries_number:
        another_entry = input()
        array_to_fill.append(another_entry)

    return array_to_fill


def sort_errors(errors_inheritance):
    errors_relation = {}
    splitted_errors = []
    for custom_class in errors_inheritance:
        splitted_errors.append(custom_class.split(':'))

    for item in splitted_errors:
        if len(item) > 1:
            errors_relation[item[0].strip()] = item[1].strip().split(' ')
        else:
            errors_relation[item[0].strip()] = ['None']

    return errors_relation


def check_requests(requests, errors_relaton):
    first_item = 0
    last_item = 1
    for request in requests:
        errors_lineage = find_ancestor(errors_relaton, request, 'None', [])
        flat_errors_lineage = list(itertools.chain.from_iterable(errors_lineage))
        if len(flat_errors_lineage) == 2 and request == flat_errors_lineage[first_item] and 'None' == flat_errors_lineage[last_item]:
            # print('nothing needed, continuing...')
            continue

        values_in_request = list(filter(lambda value: value in requests, flat_errors_lineage))
        if any(requests.index(item) < requests.index(request) for item in values_in_request):
            print(request)


def find_ancestor(errors_relaton, start, end, path):
    path = path + [start]
    if start == end:

        return [path]

    if start not in errors_relaton.keys():

        return []

    paths = []

    for node in errors_relaton[start]:
        if node not in path:
            newpaths = find_ancestor(errors_relaton, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


errors_number = int(input())
errors_inheritance = fill_dynamic_array(errors_number)
requests_number = int(input())
requests = fill_dynamic_array(requests_number)
errors_relaton = sort_errors(errors_inheritance)
check_requests(requests, errors_relaton)


