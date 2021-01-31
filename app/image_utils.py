# Reference: https://github.com/woctezuma/match-steam-banners/blob/master/generic_utils.py

import io

import numpy as np
from PIL import Image as pil_image


def get_interpolation_methods():
    interpolation_methods = {
        "nearest": pil_image.NEAREST,
        "bilinear": pil_image.BILINEAR,
        "bicubic": pil_image.BICUBIC,
    }

    return interpolation_methods


def load_image(image_filename, target_size=None, interpolation="nearest"):
    interpolation_methods = get_interpolation_methods()
    resample = interpolation_methods[interpolation]

    with open(image_filename, "rb") as f:
        img = pil_image.open(io.BytesIO(f.read()))

        if target_size is not None:
            width_height_tuple = (target_size[1], target_size[0])
            if img.size != width_height_tuple:
                img = img.resize(width_height_tuple, resample)

    return img
