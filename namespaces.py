import re
instructions_number = int(input())
instructions = []

while len(instructions) < instructions_number:
    another_instruction = input().strip()
    instructions.append(another_instruction)

namespaces = {
    'global': set()
}


def instructions_controller(instructions):
    for instruction in instructions:
        if re.match('^add', instruction):
            add_fn(instruction)
        elif re.match('^create', instruction):
            create_fn(instruction)
        elif re.match('^get', instruction):
            get_fn(instruction)
        else:
            raise Exception('Unknown instruction')


def add_fn(instruction):
    sliced_instruction = instruction.split(' ')[slice(1, None)]
    if len(sliced_instruction) == 2:
        process_variable_adding(*sliced_instruction)
    else:
        raise Exception('Enter function name and variable name')


def create_fn(instruction):
    sliced_instruction = instruction.split(' ')[slice(1, None)]
    if len(sliced_instruction) == 2:
        process_function_creating(*sliced_instruction)
    else:
        raise Exception('Enter child function name and parent function name')


def get_fn(instruction):
    sliced_instruction = instruction.split(' ')[slice(1, None)]
    if len(sliced_instruction) == 2:
        process_variable_getting(*sliced_instruction)
    else:
        raise Exception('Enter function name and variable name')


def process_variable_adding(where_to_add, variable_name):
    if where_to_add in namespaces:
        namespaces[where_to_add].add(variable_name)
    return namespaces


def process_function_creating(child_function_name, parent_function_name):
    if parent_function_name in namespaces.keys():
        namespaces[parent_function_name].add(child_function_name)
        namespaces[child_function_name] = set()
    else:
        namespaces[parent_function_name] = set()
        namespaces[parent_function_name].add(child_function_name)
        namespaces[child_function_name] = set()


def get_from_namespace(namespace, variable):
    if variable in namespaces[namespace]:
        return True
    return False


def process_variable_getting(function_name, variable_name):
    parent = function_name
    while parent is not None:
        if get_from_namespace(parent, variable_name):
            print(parent)
            return
        if parent == 'global':
            parent = None
            print('None')
        for name, scope in namespaces.items():
            if parent in scope:
                parent = name


instructions_controller(instructions)
