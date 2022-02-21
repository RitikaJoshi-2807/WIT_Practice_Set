def add_prefix_un(word):
    return ('un'+word)
def make_word_groups(vocab_words):
    prefix=vocab_words[0]
    return((' :: '+prefix).join(vocab_words))
                  
    
    
def remove_suffix_ness(word):
    index=word.find("ness")
    new_words=word[0:index]
    if(new_words[-1]=='i'):
        new_words=new_words[:-1]+"y"
    return new_words
def adjective_to_verb(sentence, index):
    k=sentence.split()
    word=k[index]
    if(word[-1]=='.'):
        word=word[:-1]
    return (word+'en')
