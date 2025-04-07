import os

def append_to_piper_metadata(filename, label, metadata_file="metadata_piper.txt"):
    # Normalize and clean
    base_filename = os.path.splitext(filename.strip())[0]
    audio_filename = f"{base_filename}.wav"
    
    # Do case-insensitive match against files in folder
    local_files = {f.lower() for f in os.listdir('.') if os.path.isfile(f)}
    
    if audio_filename.lower() not in local_files:
        print(f"❌ Error: '{audio_filename}' not found in this folder. Entry skipped.\n")
        return

    label = label.strip()
    with open(metadata_file, 'a', encoding='utf-8') as f:
        f.write(f"{base_filename}|{label}\n")
        print(f"✅ Added: {base_filename}|{label}\n")

if __name__ == "__main__":
    print("🎤 Piper Metadata Appender (Ctrl+C to stop)\n")
    try:
        while True:
            filename = input("Enter filename (e.g., gideon_0001.wav): ").strip()
            label = input("Enter label (e.g., Hello, Barry.): ").strip()
            append_to_piper_metadata(filename, label)
    except KeyboardInterrupt:
        print("\n👋 Done. Goodbye!")
