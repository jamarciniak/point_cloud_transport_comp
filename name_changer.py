import os

def rename_files(root_dir):
    for folder_name, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".csv"):
                parts = filename.split("_")
                if len(parts) >= 3 and parts[2] not in ["raw", "draco", "zlib", "zstd"]:
                    parts.insert(2, "raw")
                    new_filename = "_".join(parts)
                    old_filepath = os.path.join(folder_name, filename)
                    new_filepath = os.path.join(folder_name, new_filename)
                    os.rename(old_filepath, new_filepath)
                    print(f"Zmieniono nazwę pliku: {old_filepath} -> {new_filepath}")

root_dir = "./results"
rename_files(root_dir)
