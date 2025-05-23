from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("models/stable-diffusion")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt, output_path="static/output.png"):
    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
