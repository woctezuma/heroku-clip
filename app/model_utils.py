import torch
import clip
from utils import (
    get_device,
    get_model_and_preprocess,
    load_imagenet_classes,
    load_zeroshot_weights,
)


def compute_probs(input_image, input_text):
    model, preprocess = get_model_and_preprocess()
    image = preprocess(input_image).unsqueeze(0).to(get_device())
    text = clip.tokenize(input_text).to(get_device())

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)

        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    return probs


def predict_class(input_image, topk=(1, 5)):
    model, preprocess = get_model_and_preprocess()
    image = preprocess(input_image).unsqueeze(0).to(get_device())

    imagenet_classes = load_imagenet_classes()
    zeroshot_weights = load_zeroshot_weights()

    with torch.no_grad():
        image_features = model.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        logits = 100.0 * image_features.float() @ zeroshot_weights.float()

        pred = logits.topk(max(topk), 1, True, True)[1].t()
        if len(pred) == 1:
            predicted_class = [imagenet_classes[pred]]
        else:
            predicted_class = [imagenet_classes[i] for i in pred]

    return predicted_class
