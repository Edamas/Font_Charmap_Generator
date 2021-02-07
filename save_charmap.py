from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode


def get_FontCharmapList(fontpath):
    if fontpath.split('.')[-1] == 'ttf':    # It's a True Type font
        ttfont = TTFont(fontpath)
        chars = ''
        for indice in range(1100000):
            found = False
            for table in ttfont['cmap'].tables:
                if indice in table.cmap.keys() and not found:
                    chars += chr(indice)
                    found = True
        ttfont.close()
        return chars
    else:
        print(fontpath + ' is not a True Type Font (".ttf")')
        return ''

    
def get_fontPathslist(path_root):
    if not path_root.endswith('/'):
        path_root = path_root + '/'
    return [path_root + font_file for font_file in os.listdir(path_root) if font_file.split('.')[-1] == 'ttf']


def get_FontsCharmapsdict(font_paths):
    font_charmaps = {}
    for n, font_path in enumerate(font_paths):
        chars = get_FontCharmapList(font_path)
        font_charmaps[font_path.split('/')[-1]] = chars
    return font_charmaps


def chars2txt(output_file, chars):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(chars)
    return True


lucon = get_FontCharmapList('c:/windows/Fonts/lucon.ttf')
print(lucon)
# '\x00\x08\t\n\r\x1d !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x80\x81...'


path_root = 'c:/windows/Fonts'
font_paths = get_fontPathslist(path_root)
print(font_paths[:10])
# ['c:/windows/Fonts/arial.ttf', 'c:/windows/Fonts/arialbd.ttf', 'c:/windows/Fonts/arialbi.ttf', 'c:/windows/Fonts/ariali.ttf', ...]


fontsdict = get_FontsCharmapsdict([path for path in font_paths if 'lucon' in path])
print(fontsdict)
# {'lucon.ttf': '\x00\x08\t\n\r\x1d !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz...'}


for font in fontsdict:
    print(font, '\tSaved:', chars2txt(font.replace('.ttf', '_ttf'), fontsdict[font]))
# lucon.ttf 	Saved: True
