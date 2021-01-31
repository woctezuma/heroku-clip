import streamlit as st
from model_utils import compute_probs, predict_class
from image_utils import resize_image


def minimal_example(input_image):
    input_text = ["a diagram", "a dog", "a cat"]
    st.write("{}".format(input_text))

    probs = compute_probs(input_image, input_text)
    st.write("Label probs: {}".format(probs))

    return


def imagenet_example(input_image):
    predicted_class = predict_class(input_image)
    st.write("Predictions: {}".format(predicted_class))

    return


if __name__ == "__main__":
    st.title("Deploy OpenAI's CLIP on Heroku.")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        input_image = resize_image(uploaded_file, target_size=[224, 224])
        st.image(input_image, caption="Input", use_column_width=True)

        imagenet_example(input_image)
