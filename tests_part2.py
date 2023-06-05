

def organize_text(text):
    text = text.replace('\n', ' ').replace(',', '').lower().split('.')
    organized_text = []
    for c in text:
        if c:
            c = c.strip()
            c = c.split(' ')
            organized_text.append(c)
    return organized_text

def organize_parameters(organized_text):
    parameters = []
    for l in organized_text:
        for id2, w in enumerate(l):
            comp = []
            for pos in range(l.index(w)+1, len(l)):
                if l[pos] != w:
                    seg = [w, l[pos]]
                    comp.append(seg)

            for pos in range(l.index(w)-1,-1,-1): 
                if l[pos] != w:
                    seg = [w, l[pos]]
                    comp.append(seg)
            
            if comp:
                parameters.append(comp)

    return parameters



text = """A amizade consegue ser tão complexa.
Deixa uns desanimados, outros bem felizes.
É a alimentação dos fracos
É o reino dos fortes.

Faz-nos cometer erros
Os fracos deixam se ir abaixo
Os fortes erguem sempre a cabeça
Os assim assumem-nos.

Sem pensar conquistamos
o mundo geral
e construímos o nosso pequeno lugar,
deixando brilhar cada estrelinha.

Estrelinhas
Doces, sensíveis, frias, ternurentas.
Mas sempre presentes em qualquer parte.
Os donos da amizade."""

organized_text = organize_text(text)
#print(organized_text)
print(organize_parameters(organized_text))
