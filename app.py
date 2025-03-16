import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

# Check if GPU is available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Stable Diffusion model (cached to avoid reloading)
@st.cache(allow_output_mutation=True)
def load_model():
    model_id = "stabilityai/stable-diffusion-2-1"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
    pipe = pipe.to(device)  # Move to appropriate device
    return pipe

pipe = load_model()

# Streamlit app UI
st.title("🖼️ AI Realistic Image Generator")
st.write("Enter a text prompt to generate a realistic image!")

# User input
prompt = st.text_input("Enter your prompt (e.g., 'A futuristic city at sunset'):")
resolution = st.selectbox("Select image resolution:", ["512x512", "768x768"])

# Generate image
if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating your image (this may take a few minutes)..."):
            try:
                # Adjust resolution
                height, width = map(int, resolution.split("x"))

                # Generate the image
                with torch.no_grad():
                    image = pipe(prompt, height=height, width=width, num_inference_steps=50).images[0]

                # Display the image
                st.image(image, caption=prompt, use_column_width=True)

                # Save the image
                image.save("generated_image.png")
                st.success("✅ Image generated and saved as 'generated_image.png'!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
