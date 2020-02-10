class Text:
    def __init__(self,string):
        self.string = string

    def get_freq_of_word(self,word):
        count = 0
        words_list = self.string.lower().split()
        punc_list = [".",",",":","/","!","?",'@','#','$','%','^','&','*','-','+','+',';']
        for c,item in enumerate(words_list):
            if item[-1] in punc_list:
                words_list[c] = item[0:-1]
        for item in words_list:
            if item == word:
                count+=1
        print(f"'{word}' appears {count} times in text.")
        return count

    def most_common_word(self):
        words_list = self.string.lower().split()
        word_set = set()
        word_dict = {}
        punc_list = [".",",",":","/","!","?",'@','#','$','%','^','&','*','-','+','+',';']
        for c, item in enumerate(words_list):
            if item[-1] in punc_list:
                words_list[c] = item[0:-1]
        for item in words_list:
            if item not in word_set:
                word_set.add(item)
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        max_val = 0
        max_key = ""
        for key, val in word_dict.items():
            if val>max_val:
                max_val = val
                max_key = key

        print(f"Most common word: '{max_key}'")
        return max_key

    def get_unique_words(self):
        words_list = self.string.lower().split()
        word_set = set()
        punc_list = [".",",",":","/","!","?",'@','#','$','%','^','&','*','-','+','+',';']
        for c, item in enumerate(words_list):
            if item[-1] in punc_list:
                words_list[c] = item[0:-1]
        for item in words_list:
            if item not in word_set:
                word_set.add(item)
            elif item in word_set:
                word_set.remove(item)

        print("The words in the text that occur no more than once are:")
        print(word_set)
        return word_set


class TextModification(Text):

    def remove_punc_and_chars(self):
        words_list = self.string.lower().split()
        punc_list = [".", ",", ":", "/", "!", "?", '@', '#', '$', '%', '^', '&', '*', '-', '+', '+', ';']
        for c,item in enumerate(words_list):
            if item[-1] in punc_list:
                words_list[c] = item[0:-1]
        replaced_string = ' '.join(map(str, words_list))
        print(replaced_string)



words = '''
MOTHER died today. Or, maybe, yesterday; I can't be sure. The telegram from the 
Home says: YOUR MOTHER PASSED AWAY. FUNERAL TOMORROW. DEEP 
SYMPATHY. Which leaves the matter doubtful; it could have been yesterday. 

The Home for Aged Persons is at Marengo, some fifty miles from Algiers. With 
the two o'clock bus I should get there well before nightfall. Then I can spend the 
night there, keeping the usual vigil beside the body, and be back here by tomorrow 
evening. I have fixed up with my employer for two days' leave; obviously, under the 
circumstances, he couldn't refuse. Still, I had an idea he looked annoyed, and I said, 
without thinking: "Sorry, sir, but it's not my fault, you know." 

Afterwards it struck me I needn't have said that. I had no reason to excuse myself; 
it was up to him to express his sympathy and so forth. Probably he will do so the day 
after tomorrow, when he sees me in black. For the present, it's almost as if Mother 
weren't really dead. The funeral will bring it home to me, put an official seal on it, so 
to speak. ... 

I took the two-o'clock bus. It was a blazing hot afternoon. I'd lunched, as usual, at 
Celeste's restaurant. Everyone was most kind, and Celeste said to me, "There's no 
one like a mother." When I left they came with me to the door. It was something of a 
rush, getting away, as at the last moment I had to call in at Emmanuel's place to 
borrow his black tie and mourning band. He lost his uncle a few months ago. 

I had to run to catch the bus. I suppose it was my hurrying like that, what with the 
glare off the road and from the sky, the reek of gasoline, and the jolts, that made me 
feel so drowsy. Anyhow, I slept most of the way. When I woke I was leaning against 
a soldier; he grinned and asked me if I'd come from a long way off, and I just 
nodded, to cut things short. I wasn't in a mood for talking. 

The Home is a little over a mile from the village. I went there on foot. I asked to 
be allowed to see Mother at once, but the doorkeeper told me I must see the warden 
first. He wasn't free, and I had to wait a bit. The doorkeeper chatted with me while I 
waited; then he led me to the office. The warden was a very small man, with gray 
hair, and a Legion of Honor rosette in his buttonhole. He gave me a long look with 
his watery blue eyes. Then we shook hands, and he held mine so long that I began to 
feel embarrassed. After that he consulted a register on his table, and said: 

"Madame Meursault entered the Home three years ago. She had no private means 
and depended entirely on you." 



Albert Camus ♦ THE STRANGER 

I had a feeling he was blaming me for something, and started to explain. But he 
cut me short. 

"There's no need to excuse yourself, my boy. I've looked up the record and 
obviously you weren't in a position to see that she was properly cared for. She 
needed someone to be with her all the time, and young men in jobs like yours don't 
get too much pay. In any case, she was much happier in the Home." 

I said, "Yes, sir; I'm sure of that." 

Then he added: "She had good friends here, you know, old folks like herself, and 
one gets on better with people of one's own generation. You're much too young; you 
couldn't have been much of a companion to her." 

That was so. When we lived together, Mother was always watching me, but we 
hardly ever talked. During her first few weeks at the Home she used to cry a good 
deal. But that was only because she hadn't settled down. After a month or two she'd 
have cried if she'd been told to leave the Home. Because this, too, would have been a 
wrench. That was why, during the last year, I seldom went to see her. Also, it would 
have meant losing my Sunday — not to mention the trouble of going to the bus, 
getting my ticket, and spending two hours on the journey each way. 

The warden went on talking, but I didn't pay much attention. Finally he said: 

"Now, I suppose you'd like to see your mother?" 

I rose without replying, and he led the way to the door. As we were going down 
the stairs he explained: 

"I've had the body moved to our little mortuary — so as not to upset the other old 
people, you understand. Every time there's a death here, they're in a nervous state for 
two or three days. Which means, of course, extra work and worry for our staff." 

We crossed a courtyard where there were a number of old men, talking amongst 
themselves in little groups. They fell silent as we came up with them. Then, behind 
our backs, the chattering began again. Their voices reminded me of parakeets in a 
cage, only the sound wasn't quite so shrill. The warden stopped outside the entrance 
of a small, low building. 

"So here I leave you, Monsieur Meursault. If you want me for anything, you'll 
find me in my office. We propose to have the funeral tomorrow morning. That will 
enable you to spend the night beside your mother's coffin, as no doubt you would 
wish to do. Just one more thing; I gathered from your mother's friends that she 
wished to be buried with the rites of the Church. I've made arrangements for this; but 
I thought I should let you know." 

I thanked him. So far as I knew, my mother, though not a professed atheist, had 
never given a thought to religion in her life. 

I entered the mortuary. It was a bright, spotlessly clean room, with whitewashed 
walls and a big skylight. The furniture consisted of some chairs and trestles. Two of 
the latter stood open in the center of the room and the coffin rested on them. The lid 



Albert Camus ♦ THE STRANGER 

was in place, but the screws had been given only a few turns and their nickeled heads 
stuck out above the wood, which was stained dark walnut. An Arab woman — a 
nurse, I supposed — was sitting beside the bier; she was wearing a blue smock and 
had a rather gaudy scarf wound round her hair. 

Just then the keeper came up behind me. He'd evidently been running, as he was a 
little out of breath. 

"We put the lid on, but I was told to unscrew it when you came, so that you could 
see her." 

While he was going up to the coffin I told him not to trouble. 

"Eh? What's that?" he exclaimed. "You don't want me to ...?" 

"No," I said. 

He put back the screwdriver in his pocket and stared at me. I realized then that I 
shouldn't have said, "No," and it made me rather embarrassed. After eying me for 
some moments he asked: 

"Why not?" But he didn't sound reproachful; he simply wanted to know. 

"Well, really I couldn't say," I answered. 

He began twiddling his white mustache; then, without looking at me, said gently: 

"I understand." 

He was a pleasant-looking man, with blue eyes and ruddy cheeks. He drew up a 
chair for me near the coffin, and seated himself just behind. The nurse got up and 
moved toward the door. As she was going by, the keeper whispered in my ear: 

"It's a tumor she has, poor thing." 

I looked at her more carefully and I noticed that she had a bandage round her head, 
just below her eyes. It lay quite flat across the bridge of her nose, and one saw hardly 
anything of her face except that strip of whiteness. 

As soon as she had gone, the keeper rose. 

"Now I'll leave you to yourself." 

I don't know whether I made some gesture, but instead of going he halted behind 
my chair. The sensation of someone posted at my back made me uncomfortable. The 
sun was getting low and the whole room was flooded with a pleasant, mellow light. 
Two hornets were buzzing overhead, against the skylight. I was so sleepy I could 
hardly keep my eyes open. Without looking round, I asked the keeper how long he'd 
been at the Home. "Five years." The answer came so pat that one could have thought 
he'd been expecting my question. 

That started him off, and he became quite chatty. If anyone had told him ten years 
ago that he'd end his days as doorkeeper at a home at Marengo, he'd never have 
believed it. He was sixty- four, he said, and hailed from Paris. 

When he said that, I broke in. "Ah, you don't come from here?" 

I remembered then that, before taking me to the warden, he'd told me something 
about Mother. He had said she'd have to be buried mighty quickly because of the 



Albert Camus ♦ THE STRANGER 

heat in these parts, especially down in the plain. "At Paris they keep the body for 
three days, sometimes four." After that he had mentioned that he'd spent the best part 
of his life in Paris, and could never manage to forget it. "Here," he had said, "things 
have to go with a rush, like. You've hardly time to get used to the idea that 
someone's dead, before you're hauled off to the funeral." "That's enough," his wife 
had put in. "You didn't ought to say such things to the poor young gentleman." The 
old fellow had blushed and begun to apologize. I told him it was quite all right. As a 
matter of fact, I found it rather interesting, what he'd been telling me; I hadn't 
thought of that before. 

Now he went on to say that he'd entered the Home as an ordinary inmate. But he 
was still quite hale and hearty, and when the keeper's job fell vacant, he offered to 
take it on. 

I pointed out that, even so, he was really an inmate like the others, but he wouldn't 
hear of it. He was "an official, like." I'd been struck before by his habit of saying 
"they" or, less often, "them old folks," when referring to inmates no older than 
himself. Still, I could see his point of view. As doorkeeper he had a certain standing, 
and some authority over the rest of them. 

'''
text = TextModification(words)
# text.get_freq_of_word('the')
# text.most_common_word()
# text.get_unique_words()
text.remove_punc_and_chars()