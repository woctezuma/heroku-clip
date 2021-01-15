# Heroku CLIP

Deploy OpenAI's CLIP on Heroku.

## Usage

```bash
heroku login
heroku create
git push heroku main
```

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

<!-- Definitions -->

[openai-blog]: <https://openai.com/blog/clip/>
[openai-clip]: <https://github.com/openai/CLIP>
[openai-colab]: <https://colab.research.google.com/github/openai/clip/blob/master/Interacting_with_CLIP.ipynb>
[openai-paper]: <https://cdn.openai.com/papers/Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf>

[banner-repository-CLIP]: <https://github.com/woctezuma/steam-CLIP>
[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>

