# Font_Charmap_Generator
Generates the available charmap for one or more fonts and save it.
(Python 3.8)

## Get charmap for one font file -> list
## Get charmap for many font files -> dict
## Save charmap in fontname_ttf.txt files 
## Encoding: UTF-8

### Installing fontTools in Windows:
>  pip install --upgrade fonttools


## Examples:

#### get_FontCharmapList('c:/windows/Fonts/lucon.ttf')
'\x00\x08\t\n\r\x1d !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0¡¢£¤¥¦§¨©ª«¬\xad®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƒǺǻǼǽǾǿȘșȚțˆˇˉ˘˙˚˛˜˝;΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώЁЂЃЄЅІЇЈЉЊЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёђѓєѕіїјљњћќўџҐґẀẁẂẃẄẅỲỳ–—―‗‘’‚“”„†‡•…‰‹›‼‾⁄ⁿ₣₤₧€№™Ω⅛⅜⅝⅞←↑→↓↔↕↨∂∆∏∑−∙√∞∟∩∫≈≠≡≤≥⌂⌐⌠⌡─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬▀▄█▌▐░▒▓■▬▲►▼◄◊○◘◙☺☻☼♀♂♠♣♥♦♪♫ﬁﬂ'


#### font_paths = get_fontPathslist('c:/windows/Fonts')[:10]
['c:/windows/Fonts/arial.ttf',
 'c:/windows/Fonts/arialbd.ttf',
 'c:/windows/Fonts/arialbi.ttf',
 'c:/windows/Fonts/ariali.ttf',
 'c:/windows/Fonts/ariblk.ttf',
 'c:/windows/Fonts/bahnschrift.ttf',
 'c:/windows/Fonts/calibri.ttf',
 'c:/windows/Fonts/calibrib.ttf',
 'c:/windows/Fonts/calibrii.ttf',
 'c:/windows/Fonts/calibril.ttf']
 
 
 #### get_FontsCharmapsdict([path for path in font_paths if 'tahoma' in path])
 {
 'tahoma.ttf': ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xa0¡¢£¤¥¦§¨©ª«¬\xad®¯°±²...',
 'tahomabd.ttf': ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xa0¡¢£¤¥¦§¨©ª«¬\xad®¯°±²...'
 }
 
 
#### for font in fontsdict: print(font, '\tSaved:', chars2txt(font.replace('.ttf', '_ttf'), fontsdict[font]))
tahoma.ttf 	Saved: True
tahomabd.ttf 	Saved: True
