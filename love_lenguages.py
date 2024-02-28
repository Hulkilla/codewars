import random
    
    # example class
class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang
    def response(self, language):
        r = random.random()
        if language == self.main:
            if r < 0.85: return 'positive'
            else:        return 'neutral'
        else: # language != self.main
            if r < 0.15: return 'positive'
            else:        return 'neutral'
    

partner = TestPartner('gifts')

def love_language(partner, weeks):
    # Inicializa un contador para cada lenguaje del amor
    love_languages = {"words": 0, "acts": 0, "gifts": 0, "time": 0, "touch": 0}

    # Repite n veces (donde n es el número de semanas)
    for _ in range(7*weeks):
        language = random.choice(list(love_languages.keys()))
        if partner.response(language) == "positive":
                love_languages[language] += 1

    # Determina cuál lenguaje tiene el contador más alto
    principal_language = max(love_languages, key=love_languages.get)


    return principal_language


# Ejemplo de uso

print(love_language(partner, 6))
