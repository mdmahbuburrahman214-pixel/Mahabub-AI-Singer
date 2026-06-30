import os
import gradio as gr

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_video(image, audio):
    if image is None:
        return None, "❌ Please upload an image."

    if audio is None:
        return None, "❌ Please upload an MP3."

    return None, (
        "✅ Files received successfully.\n\n"
        "Next step: AI video generation will be connected in generate.py."
    )

demo = gr.Interface(
    fn=generate_video,
    inputs=[
        gr.Image(type="filepath", label="📷 Upload Photo"),
        gr.Audio(type="filepath", label="🎵 Upload MP3")
    ],
    outputs=[
        gr.Video(label="🎬 AI Video"),
        gr.Textbox(label="Status")
    ],
    title="Mahabub AI Singer Studio",
    description="Upload a photo and an MP3 to generate a talking AI video."
)

if __name__ == "__main__":
    demo.launch()
