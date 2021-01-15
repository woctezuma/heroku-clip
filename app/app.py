import streamlit as st
import torch
import clip
from PIL import Image

def get_device():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return device

@st.cache
def cached_model():
    model, preprocess = clip.load("ViT-B/32", device=get_device())
    return model, preprocess

device = get_device()
model, preprocess = cached_model()

st.title("Deploy OpenAI's CLIP on Heroku.")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)    
    st.image(image, caption="Input", use_column_width=True)
    
    input_text = ["a diagram", "a dog", "a cat"]
    st.write('{}'.format(input_text))   

    image = preprocess(input_image).unsqueeze(0).to(device)
    text = clip.tokenize(input_text).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
    
    logits_per_image, logits_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    st.write("Label probs:".format(probs))

