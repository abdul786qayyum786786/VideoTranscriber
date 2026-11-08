import tkinter as tk
from tkinter import filedialog
import os
import threading
from faster_whisper import WhisperModel

# Whisper model
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

selected_video_path = None

# Tkinter window
window = tk.Tk()

window.title("Video Transcriber")
window.geometry("600x400")
window.resizable(False, False)


# Main heading
label = tk.Label(
    window,
    text="Video Transcriber",
    font=("Arial", 24)
)

label.pack(pady=(45, 30))


# Select video function
def select_video():
    global selected_video_path

    video_file = filedialog.askopenfilename(
        title="Select a Video",
        filetypes=[
            ("Video Files", "*.mp4 *.mkv *.avi *.mov *.webm"),
            ("All Files", "*.*")
        ]
    )

    if video_file:
        selected_video_path = video_file
        video_name = os.path.basename(video_file)

        max_length = 50

        if len(video_name) > max_length:
            video_name = video_name[:47] + "..."

        selected_video_label.config(
            text=f"Selected Video: {video_name}"
)

        print("Selected video:")
        print(video_file)


# Select Video button
button = tk.Button(
    window,
    text="Select Video",
    font=("Arial", 14),
    width=15,
    command=select_video
)

button.pack(pady=5)

# Selected video label
selected_video_label = tk.Label(
    window,
    text="No video selected",
    font=("Arial", 12)
)

selected_video_label.pack(pady=(12, 18))

# Save Transcription File
def save_transcription(transcription_text):
    video_name = os.path.splitext(
        os.path.basename(selected_video_path)
    )[0]

    save_path = filedialog.asksaveasfilename(
        title="Save Transcription",
        defaultextension=".txt",
        initialfile=f"{video_name}.txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(transcription_text)

        status_label.config(
            text="Status: Transcription saved"
        )
    else:
        status_label.config(
            text="Status: Save cancelled"
        )

# Format timestamp as HH:MM:SS
def format_timestamp(seconds):
    total_seconds = int(round(seconds))

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Transcribe Selected Video
def transcribe_video():
    if selected_video_path is None:
        status_label.config(
            text="Status: Please select a video first"
        )
        return

    status_label.config(
        text="Status: Transcribing..."
    )

    def run_transcription():
        video_file = selected_video_path

        segments, info = model.transcribe(video_file)

        transcription_text = ""

        for segment in segments:
            start = format_timestamp(segment.start)
            end = format_timestamp(segment.end)

            transcription_text += (
                f"[{start} - {end}] "
                f"{segment.text.strip()}\n"
            )

        window.after(
            0,
            lambda: save_transcription(transcription_text)
        )

    threading.Thread(
        target=run_transcription,
        daemon=True
    ).start()

# Transcribe button
transcribe_button = tk.Button(
    window,
    text="Transcribe",
    font=("Arial", 14),
    width=15,
    command=transcribe_video
)

transcribe_button.pack(pady=5)

# Status label
status_label = tk.Label(
    window,
    text="Status: Ready",
    font=("Arial", 11)
)

status_label.pack(pady=(18, 0))

window.mainloop()