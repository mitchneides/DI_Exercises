

class AnagramChecker:

    def __init__(self):
        self.wordlist = open("sowpods.txt","r").read()
        self.wordlist = self.wordlist.split('\n')

    def is_valid_word(self,word):
        return True if word in self.wordlist else False

    def get_anagrams(self,word):
        anagram_list = []
        for item in self.wordlist:
            if word != item and "".join(sorted(word)) == "".join(sorted(item)):
                anagram_list.append(item)

        if len(anagram_list) > 0:
            return anagram_list
        else:
            return 'None'

    def check_if_anagram(self,word1,word2):
        return True if word1 != word2 and "".join(sorted(word1)) == "".join(sorted(word2)) else False



if __name__ == "__main__":
    ana = AnagramChecker()
    print(ana.is_valid_word("HELLO"))
    print(ana.get_anagrams('TEAM'))
    print(ana.check_if_anagram('CAR','ARC'))
    print(ana.check_if_anagram('CAR','ART'))

