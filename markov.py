from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    #reading_the_file = open(file_path)
    reading_the_file = open(file_path)
    text_string = reading_the_file.read()

    return text_string #"This should be a variable that contains your file text as one long string"


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

   
    text_list = text_string.split("\n")
    
    word_list = []
    for sentences in text_list:
        words = sentences.split(' ')
        for word in words:
            word_list.append(word)

    chains = {}
    # word_three_list = []
    for i in range((len(word_list)-2)):
        key = (word_list[i], word_list[i+1])
        word_three = word_list[i+2]  

        if key not in chains:        
            chains[key] = [word_three]            

        else:       
            chains[key].append(word_three)

    # print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    fake_text = []
    starting_tuple = choice(chains.keys())
    fake_text.append(starting_tuple)
    
    # fake_text.append(random_word)

    while key in chains:
        random_word = choice(chains[starting_tuple])

        if random_word == key[0]:
            fake_text.append(key)
        #break


    print fake_text

    # fake_text.append(starting_tuple)

    # print chains[starting_tuple]

    # while chains[key[0]] != "Sam":
        
    #     fake_text.append(random_word)
    #     if random_word == key[0]:
    #         fake_text.append(key)
        
            

    #print fake_text        

    # your code goes here
    
    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
