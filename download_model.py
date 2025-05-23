from diffusers import StableDiffusionPipeline

token = "your_huggingface_token_here"  # paste your token string

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    use_auth_token=token
)
pipe.save_pretrained("models/stable-diffusion")
