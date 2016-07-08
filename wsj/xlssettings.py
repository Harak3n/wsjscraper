from xlwt import *

fnt = Font()
fnt.name = 'Arial'

fntRed = Font()
fntRed.name = 'Arial'
fntRed.colour_index = 3

fntGreen = Font()
fntGreen.name = 'Arial'
fntGreen.colour_index = 2

style = XFStyle()
style.font = fnt

styleRed = XFStyle()
styleRed.font = fntRed

styleGreen = XFStyle()
styleGreen.font = fntGreen
