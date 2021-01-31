import json
import torch
import clip
import numpy as np


def get_device():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    return device


def get_model_and_preprocess():
    model, preprocess = clip.load("ViT-B/32", device=get_device())

    return model, preprocess


def get_imagenet_classes_filename():
    return "data/imagenet_classes.json"


def load_imagenet_classes():
    with open(get_imagenet_classes_filename(), "r") as f:
        imagenet_classes = json.load(f)
    return imagenet_classes


def get_zeroshot_weights_filename():
    return "data/zeroshot_weights.npy"


def load_zeroshot_weights():
    zeroshot_weights_for_cpu = np.load(get_zeroshot_weights_filename())
    zeroshot_weights_for_gpu = zeroshot_weights_for_cpu.to(get_device())
    return zeroshot_weights_for_gpu


def save_zeroshot_weights(zeroshot_weights_for_gpu):
    zeroshot_weights_for_cpu = zeroshot_weights_for_gpu.cpu().numpy()
    np.save(get_zeroshot_weights_filename(), zeroshot_weights_for_cpu)
    return
