import os
import gradio as gr
from sadtalker_runner import generate

# Create required folders
os.makedirs("assets/input", exist_ok=True)
os.makedirs("assets/output", exist_ok=True)


def create_video(image_path, audio_path):
    """
    Generate talking face video using SadTalker.
    """

    if image_path is None:
        raise gr.Error("Please upload an image.")

    if audio_path is None:
        raise gr.Error("Please upload an audio file.")

    output = generate(image_path, audio_path)

    if os.path.isdir(output):
        videos = [
            os.path.join(output, f)
            for f in os.listdir(output)
            if f.endswith(".mp4")
        ]

        if len(videos) == 0:
            raise gr.Error("No video generated.")

        return videos[0]

    if os.path.isfile(output):
        return output

    raise gr.Error("Output video not found.")


with gr.Blocks(
    title="Mahabub AI Singer Studio"
) as demo:

    gr.Markdown(
        """
# 🎤 Mahabub AI Singer Studio

Generate AI Talking/Singing Video from a Portrait Image and Audio.
"""
    )

    with gr.Row():

        image = gr.Image(
            type="filepath",
            label="Portrait Image"
        )

        audio = gr.Audio(
            type="filepath",
            label="MP3 / WAV Audio"
        )

    generate_btn = gr.Button(
        "🎬 Generate Video",
        variant="primary"
    )

    output = gr.Video(
        label="Generated Video"
    )

    generate_btn.click(
        fn=create_video,
        inputs=[image, audio],
        outputs=output
    )

    gr.Markdown(
        """
---
Mahabub AI Singer Studio v1.0
"""
    )

if __name__ == "__main__":
    demo.launch(
        share=True,
        debug=True
    )
