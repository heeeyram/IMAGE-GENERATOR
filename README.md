# 🧠 AI Image Generator with Streamlit 🎨

This is a simple web application that lets you generate stunning AI images from text prompts using a text-to-image model. The app is built using **Streamlit** for fast deployment and a friendly UI.

---

## 🚀 Features

- 📝 Enter any creative text prompt
- 🖼️ Generate high-quality AI images
- 💾 Option to download generated images
- 🌐 Easy to run locally using Streamlit

---

## 📦 Tech Stack

- **Python**
- **Streamlit** – for web interface
- **OpenAI / Stability API** or custom model (depends on what you're using)
- **Pillow / Requests** – for image processing

---

## 🧠 How It Works

1. User enters a text prompt (e.g. *"a fantasy castle on a mountain during sunset"*).
2. The app sends the prompt to the image generation API.
3. The AI model returns a generated image.
4. Streamlit displays it instantly, with a download option.

---

## 🖥️ How to Run Locally

```bash
git clone https://github.com/heeeyram/IMAGE-GENERATOR
cd ai-image-generator
pip install -r requirements.txt
streamlit run app.py
