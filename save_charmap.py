from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import os

def saveCharmap(path, outpath):
    fontes = os.listdir(path)
    generated = []
    for n, fonte in enumerate(fontes):
        if fonte.split('.')[-1] == 'ttf':
            fontepath = path + fonte
            font = TTFont(fontepath)
            chars = []
            for indice in range(1100000):
                char = chr(indice)
                for table in font['cmap'].tables:
                    if indice in table.cmap.keys():
                        if char not in chars:
                            chars += char
            font.close()
            with open(outpath + fonte.replace('.', '_') + '.txt', 'w', encoding='utf-8') as f:
                f.write(chars)
            print(len(chars), '\t', fontepath)
        generated.append(fonte)
    return generated

path = 'c:/windows/Fonts/'
outpath = 'charmaps/'
saveCharmap(path, outpath)
