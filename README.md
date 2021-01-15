# Heroku CLIP

Deploy OpenAI's CLIP on Heroku.

## Usage

```bash
heroku login
heroku create
git push heroku main
```

## Recommendation: use Colab instead

I have noticed in logs that the app uses too much memory:

> Process running mem=834M(162.9%)
> Error R14 (Memory quota exceeded)

Moreover, the app is slow because it does not have access to a GPU on Heroku.

If a [REST API][wiki-REST-API] is not required, I would recommend to use Colab instead:
-   the notebook can be user-friendly,
-   memory is less constrained,
-   a GPU will be available for free.

## References

-   Open AI's CLIP (Contrastive Language-Image Pre-Training):
    - [Official blog post][openai-blog]
    - [Official Github repository][openai-clip]
    - [Official Colab notebook][openai-colab]
      [![Open In Colab][colab-badge]][openai-colab]
    - [Radford, Alec, et al. *Learning Transferable Visual Models From Natural Language Supervision*. arXiv 2021.][openai-paper]
-   My usage of CLIP:
    - [`steam-CLIP`][banner-repository-CLIP]: retrieve games with similar banners, using OpenAI's CLIP (resolution 224),
    - [`heroku-clip`][heroku-app-CLIP]: deploy CLIP on Heroku.
-   Examples of interactive applications:
    - using Streamlit: [`ternaus/retinaface_demo`][streamlit-app]
     - caveat: there is no GPU because of deployment to Heroku,
     - to use a GPU, you will need to install PyTorch, then run the app locally,
    - using Flask: [`matsui528/sis`][flask-app]
     - caveat: a priori no GPU for the same reason as with Streamlit,
     - to use a GPU, you will need to install Tensforlow 2, then run the app locally,
    - using Node.js: [`rom1504/image_embeddings`][nodejs-app]
     - caveat:
      - embedding has to be pre-computed and downloaded by the user,
      - the user won't be able to compute the embedding for any image query on the fly,
     - trivia:
      - 4.88 MB .npy for 1000 vectors of dimension 1280,
      - potentially up to 60 MB .npy for 30k vectors of dimension 512.
     - using Colab: [`tg-bomze/Face-Depixelizer`][colab-app-equivalent]
      - caveat: the user has to log in with a Google account,
      - there is access to a free GPU.
      
[streamlit-app]: <https://github.com/ternaus/retinaface_demo>
[flask-app]: <https://github.com/matsui528/sis>
[nodejs-app]: <https://github.com/rom1504/image_embeddings/tree/web>
[colab-app-equivalent]: <https://github.com/tg-bomze/Face-Depixelizer>

<!-- Definitions -->

[openai-blog]: <https://openai.com/blog/clip/>
[openai-clip]: <https://github.com/openai/CLIP>
[openai-colab]: <https://colab.research.google.com/github/openai/clip/blob/master/Interacting_with_CLIP.ipynb>
[openai-paper]: <https://cdn.openai.com/papers/Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf>

[banner-repository-CLIP]: <https://github.com/woctezuma/steam-CLIP>
[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>

[wiki-REST-API]: <https://en.wikipedia.org/wiki/Representational_state_transfer>

