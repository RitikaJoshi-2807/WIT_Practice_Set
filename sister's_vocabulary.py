def add_prefix_un(word):
    return ('un'+word)
def make_word_groups(vocab_words):
    prefix=vocab_words[0]
    return((' :: '+prefix).join(vocab_words))
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """



def remove_suffix_ness(word):
    index=word.find("ness")
    new_words=word[0:index]
    if(new_words[-1]=='i'):
        new_words=new_words[:-1]+"y"
    return new_words
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """

   

    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

   


def adjective_to_verb(sentence, index):
    k=sentence.split()
    word=k[index]
    if(word[-1]=='.'):
        word=word[:-1]
    return (word+'en')
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
