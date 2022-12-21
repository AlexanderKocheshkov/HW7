#В задании не было указано количество цветов
rgb = {
    "black": (0,0,0),
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "yellow": (255,255,0),
    "aqua": (0,255,255),
    "purpur": (255,0,255),
    "silver": (192,192,192),
    "gray": (128,128,128),
    "oliva": (128,128,0),
    "orange red": (255,69,0)
}
for key, value in rgb.items():
    print("Color: ", key, "Code:", value)