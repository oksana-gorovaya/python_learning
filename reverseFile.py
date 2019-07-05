"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке."""
with open(input(), 'r') as input_file:
	initial_dataset = [line.strip() for line in input_file.readlines()]


def reverse_file_content(initial_dataset):
	initial_dataset.reverse()
	if initial_dataset[0] == '':
		initial_dataset.remove('')
	return initial_dataset


reversed_dataset = reverse_file_content(initial_dataset)


with open(input(), 'w') as reply:
	for line in reversed_dataset:
		reply.write(line + '\n')