l = ["listen", "silent", "enlist", "hello", "world","lohel"]
anagram_dict = {}
not_anagram = []

for word in l:
    sorted_word = tuple(sorted(word))
    print(sorted_word)
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]

# Separate anagrams and non-anagrams
anagrams = {k: v for k, v in anagram_dict.items() if len(v) > 1}
not_anagrams = [v[0] for k, v in anagram_dict.items() if len(v) == 1]

print("Anagram groups:", anagrams)
print("Not Anagram words:", not_anagrams)