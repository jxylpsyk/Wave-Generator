# Used to determine whether the numbers in the graph image should be black or white


from matplotlib.colors import hex2color

def __round(num, decimal=0):
    return int(num * 10**decimal)/10**decimal

def __hex2rgb(hex_val):
    return (hex2color(hex_val)[0] * 255, hex2color(hex_val)[1] * 255, hex2color(hex_val)[2] * 255)

def black_or_white(hex_val):

    c_list = __hex2rgb(hex_val)
    luminosity = c_list[0] * 0.299 + c_list[1] * 0.587 + c_list[2] * 0.114


    return "#000000" if __round(luminosity) >= 128 else "#ffffff"


