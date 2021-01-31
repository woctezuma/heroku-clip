# Reference: https://colab.research.google.com/github/openai/clip/blob/master/notebooks/Prompt_Engineering_for_ImageNet.ipynb

import torch
import clip
from tqdm import tqdm
from utils import (
    get_device,
    get_model_and_preprocess,
    load_imagenet_classes,
    load_zeroshot_weights,
    save_zeroshot_weights,
)
from imagenet_templates import load_imagenet_templates


def zeroshot_classifier(classnames, templates):
    model, preprocess = get_model_and_preprocess()

    with torch.no_grad():
        zeroshot_weights = []
        for classname in tqdm(classnames):
            texts = [
                template.format(classname) for template in templates
            ]  # format with class
            texts = clip.tokenize(texts).to(get_device())  # tokenize
            class_embeddings = model.encode_text(texts)  # embed with text encoder
            class_embeddings /= class_embeddings.norm(dim=-1, keepdim=True)
            class_embedding = class_embeddings.mean(dim=0)
            class_embedding /= class_embedding.norm()
            zeroshot_weights.append(class_embedding)
        zeroshot_weights = torch.stack(zeroshot_weights, dim=1).to(get_device())
    return zeroshot_weights


def compute_zeroshot_weights():
    imagenet_classes = load_imagenet_classes()
    imagenet_templates = load_imagenet_templates()
    zeroshot_weights = zeroshot_classifier(imagenet_classes, imagenet_templates)
    return zeroshot_weights


def get_zeroshot_weights():
    try:
        zeroshot_weights = load_zeroshot_weights()
    except FileNotFoundError:
        zeroshot_weights = compute_zeroshot_weights()
        save_zeroshot_weights(zeroshot_weights)
    return zeroshot_weights


if __name__ == "__main__":
    zeroshot_weights = get_zeroshot_weights()
