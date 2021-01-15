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

<!-- Definitions -->

[openai-blog]: <https://openai.com/blog/clip/>
[openai-clip]: <https://github.com/openai/CLIP>
[openai-colab]: <https://colab.research.google.com/github/openai/clip/blob/master/Interacting_with_CLIP.ipynb>
[openai-paper]: <https://cdn.openai.com/papers/Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf>

[banner-repository-CLIP]: <https://github.com/woctezuma/steam-CLIP>
[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>

[wiki-REST-API]: <https://en.wikipedia.org/wiki/Representational_state_transfer>

