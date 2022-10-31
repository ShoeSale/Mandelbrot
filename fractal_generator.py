from mandelbrot import MandelbrotSet
from viewport import Viewport
from PIL import Image
from PIL.ImageColor import getrgb
import os, re

def main():
    mandelbrot_set = MandelbrotSet(max_iterations=60, escape_radius=1000)

    resolution = quality()
    name = valid_input_name("File Name: ")

    image = Image.new(mode="RGB", size=resolution)
    for pixel in Viewport(image, center=(-.75), width=4):
        stability = mandelbrot_set.stable(complex(pixel), smooth=True)
        if stability == 1:
            pixel.color = (255, 255, 255)
        else:
            pixel.color = hsb(
                hue_degrees= int((stability) * 360),
                saturation=1-stability,
                brightness=0.6
            )
        image_dir = f"{os.path.dirname(os.path.realpath(__file__))}/images"
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    image.save(f"{image_dir}/{name}.jpg")

    image.show()

def valid_input_name(s: str) -> str:
    while True:
        name = input(s)
        if match := re.fullmatch(r"\w+",name):
            return match.group()
        else:
            print(f"\"{name}\" is not a valid name")
            continue

def quality():
    '''Func defines image resolution'''
    resolution_dict = {
        "sd": (1280, 720),
        "hd": (1920, 1080),
        "uhd":(3840, 2160),
        "mega": (10000, 10000)
        }
    match i:= input("SD, HD or UHD? >_").lower():
        case "sd":
            return resolution_dict[i]
        case "hd":
            return resolution_dict[i]
        case "uhd":
            return resolution_dict[i]
        case "mega":
            return resolution_dict[i]
        case _:
            raise ValueError('Resolution not found')

def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stabiliity = mandelbrot_set.stable(complex(pixel), smooth)
        index = int(min(stabiliity * len(palette), len(palette)-1))
        pixel.color = palette[index % len(palette)]
            
def denormalize(palette):
    return [
    tuple(int(channel * 255) for channel in color)
    for color in palette
    ]

def hsb(hue_degrees: int, saturation: float, brightness: float):
    hue = hue_degrees+120 % 360
    saturation = saturation * 100
    brightness = brightness * 100
    rgb = getrgb(f"hsv({hue},{saturation}%,{brightness}%)")
    return rgb



if __name__ == "__main__":
    main()