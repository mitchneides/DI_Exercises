class Book:
    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text
        self.sentences = self.text.split('. ')

    def __repr__(self): #repr(esentation) defines what will be displayed when print is called
        return f"Book: {self.title} by {self.author}"

    def __add__(self, other):
        return Book(title=self.title + ' & ' + other.title,
                    author=self.author + ' & ' + other.author,
                    text=self.text + '\n' + other.text)

    def __len__(self):
        return len(self.text)

    def __mul__(self, other):
        if type(other) == int:
            return [self]*other
        elif isinstance(other, Book): #checks if 'other' is an instance of book
            return [self]*len(other)

    def __gt__(self, other):
        if isinstance(other, Book):
            return len(self) > len(other)
        else:
            raise TypeError("Unsupported operation")

    def __lt__(self, other):
        if isinstance(other, Book):
            return len(self) < len(other)
        else:
            raise TypeError("Unsupported operation")

    def __getitem__(self, item):
        return self.sentences[item]

    def __iter__(self):
        self.i = 0
        return self
#iter must be followed by next to control getting to the next round
    def __next__(self):
        if self.i >= len(self.sentences):
            raise StopIteration
        else:
            out = self.sentences[self.i]
            self.i += 1
            return out



if __name__ == '__main__':
    zohar = Book(title="The Zohar", author="Rabbi Shimon bar Yohai", text="asdfad kjasdf. asdfadf. asdfha asdhfoaiuhd asdoiufhasdf asdfhiuh. apsidfpaosidjfpoaj asdfapoisjdf")
    # print(zohar) #because of our redefining of __repr__ we get the customized info instead of the memory location
    lotr = Book(title="Lord of the Rings", author="JR Tolkien", text=".............")
    # print(zohar + lotr) #customized by changing print def and addition def
    # print(zohar*3) #customized by changing print def and mult def
    # print(zohar*lotr)
    print(zohar>lotr)
    print(zohar<lotr)

    for something in zohar:
        print(something)

    print(zohar[0]) #customized by redefining __getitem__


    with open('the_stranger.txt','r') as file:
        text = file.read()

    print(text) #outside with so file is already closed, but was already read by comp

    with open('my_book.txt','w') as file:
        file.write("asdf asdfad asdfasdf")

    stranger = Book("The Stranger", 'Some Author', text)
    print(stranger)
    for sentence in stranger:
        print(sentence)
    print(len(stranger))
