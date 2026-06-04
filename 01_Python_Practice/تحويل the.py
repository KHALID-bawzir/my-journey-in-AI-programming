from typing import List
def replaceThe(txt: str):
    words = txt.split()
    an = ['a' , 'i' , 'e' , 'o' , 'u']
    for i in range(len(words) - 1):
        if words[i].lower() == 'the':
            clen_word = words[i + 1].strip('.,?/!')
            if clen_word and clen_word[0].lower() in an:
                words[i] = 'an'
            else:
                words[i] = 'a'
    return ' '.join(words)
print(replaceThe('race the car'))
