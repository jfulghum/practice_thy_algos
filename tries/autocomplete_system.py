# https://leetcode.com/problems/design-search-autocomplete-system/

class AutocompleteSystem:
	def __init__(self, sentences: List[str], times: List[int]):
		self.root = {}
		for sentence, count in zip(sentences, times):
			self.register(sentence, count)
		self.curr_input = []
		self.curr_node = self.root

	def register(self, sentence, count):
		node = self.root
		for char in sentence:
			node = node.setdefault(char, {"cnt":{}})
			node["cnt"][sentence] = node["cnt"].get(sentence, 0) + count

	def input(self, c: str) -> List[str]:
		if c == "#":
			self.register(''.join(self.curr_input), 1)
			self.curr_input = []
			self.curr_node = self.root
			return []
		else:
			self.curr_input.append(c) 
			if self.curr_node and c in self.curr_node:
				self.curr_node = self.curr_node[c]
				heap = [(-count, sentence) for sentence,count in self.curr_node["cnt"].items()]
				return [res[1] for res in heapq.nsmallest(3, heap)]
			else:
				self.curr_node = None
				return []
