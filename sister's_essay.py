def capitalize_title(title):
    new=title.split()
    knew=[i.title() for i in new]
    title=" ".join(knew)
    return title
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """

    


def check_sentence_ending(sentence):
    sentence=str(sentence)
    for item in sentence:
        if (sentence.endswith(".")):
            return True
        else:
            return False
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    


def clean_up_spacing(sentence):
    new=sentence.split()
    sentence=" ".join(new)
    return sentence
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """

    


def replace_word_choice(sentence, old_word, new_word):
    sentence_new=sentence.replace(old_word,new_word)
    return sentence_new
    """

    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words
    """
 
