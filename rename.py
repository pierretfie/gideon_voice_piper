import os

def rename_gideon_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith('.wav')]
    files.sort()

    for index, filename in enumerate(files, start=1):
        new_name = f"gideon_{index:04d}.wav"

        # Skip renaming if filename is already correct
        if filename == new_name:
            continue

        # Handle conflict
        if os.path.exists(new_name):
            # Option 1: Append a suffix (e.g., _conflict)
            base, ext = os.path.splitext(new_name)
            new_name = f"{base}_conflict{ext}"
            print(f"[Conflict] {new_name} exists — renaming to: {new_name}")

            # Option 2 (instead): Skip or overwrite
            # print(f"[Skipping] {new_name} already exists.")
            # continue
            # os.remove(new_name)  # overwrite if desired

        print(f"Renaming: {filename} → {new_name}")
        os.rename(filename, new_name)

if __name__ == "__main__":
    rename_gideon_files()
