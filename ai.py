import torch
from diffusers import StableDiffusionPipeline
import os

pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
pipe = pipe.to('cuda' if torch.cuda.is_available() else 'cpu')

def generate_image(prompt, file_path):
    if not os.path.exists(file_path):
        images = pipe(prompt,
                    height=480,
                    width=480,
                    torch_dtype=torch.float16,
                    revision = "fp16",
                    num_inference_steps = 25,  # Higher the better but slower
                    guidance_scale = 7.5,
                    num_images_per_prompt = 1).images
        images[0].save(file_path)
    else:
        print(f'File {file_path} already exists')

if __name__ == '__main__':
    # Test
    generate_image('chinese university', 'static/chinese university.jpg')