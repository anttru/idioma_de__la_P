def to_p_sentence(sentence):
    cypher = {"a" : "apa", "e" : "epe", "i" : "ipi", "o" : "opo", "u" : "upu"}
    translation = ""
    for character in sentence:
        if character in cypher:
            translation +=  cypher[character]
        else:
            translation += character
    return translation

def from_p(sentence):
    cypher = {"apa" : "a", "epe" : "e", "ipi" : "i", "opo" : "o", "upu" : "u"}
    translation = ""
    position = 0
    if sentence != "":
        while position < len(sentence):
            if position < len(sentence) - 2:
                if sentence[position : position + 3] in cypher:
                    translation += cypher[sentence[position : position + 3]]
                    position += 2
                else:
                    translation +=  sentence[position]
            else:
                translation += sentence[position]
            position += 1
    else:
        translation = ""
        
    return translation

a = "esto es una prueba"

print(to_p_sentence(a))

print(from_p(to_p_sentence(a)))
