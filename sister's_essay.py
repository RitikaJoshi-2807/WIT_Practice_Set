def capitalize_title(title):
    new=title.split()
    knew=[i.title() for i in new]
    title=" ".join(knew)
    return title
    
def check_sentence_ending(sentence):
    sentence=str(sentence)
    for item in sentence:
        if (sentence.endswith(".")):
            return True
        else:
            return False
def clean_up_spacing(sentence):
    new=sentence.split()
    sentence=" ".join(new)
    return sentence
    
    
def replace_word_choice(sentence, old_word, new_word):
    sentence_new=sentence.replace(old_word,new_word)
    return sentence_new
 
