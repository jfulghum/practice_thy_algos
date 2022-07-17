# complex solution
from collections import defaultdict

def groupAnagrams(words):
    sorted_words = defaultdict(list)
    for i, word in enumerate(words):
        sorted_word = "".join(sorted(list(word)))
        if sorted_words.get(sorted_word) is None:
            sorted_words[sorted_word] = [i]
        else:
            sorted_words[sorted_word].append(i)
    result = []  
    tempwords = []
  
    for key, index in sorted_words.items():
        for i in index:
          tempwords.append(words[i])
          
        result.append(tempwords)
        tempwords = []
    return result

# better solution
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]

    return list(anagrams.values())
