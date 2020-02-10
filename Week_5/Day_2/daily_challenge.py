class Text:
    def __init__(self,string):
        self.string = string

    def get_freq_of_word(self,word):
        count = 0
        words_list = self.string.split()
        for item in words_list:
            if item == word:
                count+=1
        print(f"'{word}' appears {count} times in text.")
        return count

    def most_common_word(self):
        


words = 'asdfad asdfa asdfa'
text = Text(words)
text.get_freq_of_word('asdf')