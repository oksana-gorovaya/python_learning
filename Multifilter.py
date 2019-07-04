class Multifilter:
	def judge_half(self, pos, neg):
		if pos >= neg:
			return True

	def judge_any(self, pos, neg):
		if pos >= 1:
			return True

	def judge_all(self, pos, neg):
		if neg == 0:
			return True

	def __init__(self, iterable, *funcs, judge=judge_any):
		self.iterable = iterable
		self.funcs = funcs
		self.judge = judge

	def __iter__(self):

		for item in self.iterable:
			pos = 0
			neg = 0
			for func in self.funcs:
				if func(item):
					pos += 1
				else:
					neg += 1
			if self.judge(self, pos, neg):
				yield item


def mul2(x):
	return x % 2 == 0

def mul3(x):
	return x % 3 == 0

def mul5(x):
	return x % 5 == 0

a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
print(list(Multifilter(a, mul2, mul3, mul5)))
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))