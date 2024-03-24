import torch
from diffusers import StableDiffusionPipeline
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

model_id = 'stabilityai/stable-diffusion-2-1'
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to('cuda' if torch.cuda.is_available() else 'cpu')

def generate_image(prompt, file_path):
    images = pipe(prompt,
                  width=240,
                  height=240,
                  torch_dtype=torch.float16,
                  num_inference_steps = 25,  # Higher the better but slower
                  revision = "fp16",
                  guidance_scale = 9,
                  num_images_per_prompt = 1).images
    images[0].save(file_path)

if __name__ == '__main__':
    # Test
    generate_image('Hong Kong', 'static/chinese university.jpg')