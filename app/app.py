import streamlit as st
import torch
import clip
from PIL import Image


def get_device():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    return device


def get_model_and_preprocess():
    model, preprocess = clip.load("ViT-B/32", device=get_device())

    return model, preprocess


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


st.title("Deploy OpenAI's CLIP on Heroku.")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Input", use_column_width=True)

    input_text = ["a diagram", "a dog", "a cat"]
    st.write("{}".format(input_text))

    probs = compute_probs(input_image, input_text)
    st.write("Label probs: {}".format(probs))
