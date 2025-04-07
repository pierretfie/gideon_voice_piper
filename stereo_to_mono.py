from pydub import AudioSegment
import os

source_dir = "/my_gideon_dataset/"
converted_dir = "/my_gideon_dataset/wavs"

os.makedirs(converted_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.endswith(".wav"):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(converted_dir, filename)

        try:
            audio = AudioSegment.from_wav(src_path)
            audio = audio.set_channels(1)        # Convert to mono
            audio = audio.set_frame_rate(22050)  # Resample to 22,050 Hz
            audio.export(dst_path, format="wav")
            print(f"✅ Converted: {filename}")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")
