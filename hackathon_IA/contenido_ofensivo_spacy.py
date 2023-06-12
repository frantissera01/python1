import spacy

nlp = spacy.load("es_core_news_sm")

contenido_alarmante = []

contenido_ofensivo = []

lista_suicida = []

potencial_suicida = False

ofensivo = False

docInput = nlp(input("Introduzca texto a analizar: "))

docOfensivo = ["gordo","zorra", "perra", "gato", "maricon", "negro", "matate", "imbecil", "idiota", "boludo", "pelotudo", "pobre", "turro", "rata", "cagon", "retrasado", "mogolico", "gil", "gorreado", "pajero", "croto", "atorrante", "subnormal"]

docSuicida = ["cortar","ahorcar", "morirme", "morir", "suicidio", "venas", "vena" "tiro", "arma", "depresion","deprimido","deprimida" "flagelar", "sobredosis", "apuñalar", "apuñalen", "inyectar", "ahogar", "cuello", "pegar", "tirar"]

contenidoSuicida = []

"""for token in doc:
    print(token, token.lemma_)
    print("-"*3)"""

for palabra in docInput:
    palabra = str(palabra)
    for palabra_ofensivo in docOfensivo:   
        if palabra == palabra_ofensivo:
            ofensivo = True
            contenido_ofensivo.append(palabra)

print("""
Este usuario ha sido ofensivo en su comentario
Palabras ofensivas encontradas:
        """)
for palabra in contenido_ofensivo:
    print(palabra)
    print("-"*3)
    


for palabra in docInput:
    palabra = str(palabra)
    for palabra_suicida in docSuicida:
        if palabra == "cortar":
            for suicida in docSuicida:
                if suicida == "venas" or suicida == "vena":
                    potencial_suicida = True
                    lista_suicida.append(palabra)
                if suicida == "cuello":
                    potencial_suicida = True
                    lista_suicida.append(palabra)
        if palabra_suicida == "pegar":
            for suicida in docSuicida:
                if suicida == "tiro" or suicida == "tiros":
                    potencial_suicida = True
                    lista_suicida.append(palabra)
        elif palabra_suicida == palabra:
            potencial_suicida = True
            lista_suicida.append(palabra)
                    
if potencial_suicida:
    print("""
Mensaje suicida
Palabras suicidas encontradas: 
          """)
    for palabra_s in lista_suicida:
        print(palabra_s)
        print("-"*3)
        