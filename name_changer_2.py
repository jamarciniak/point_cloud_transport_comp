import os

def rename_files(root_dir):
    for folder_name, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".csv"):
                parts = filename.split("_")
                if len(parts) >= 3 and "raw" in parts and "msg" in parts:
                    raw_index = parts.index("raw")
                    msg_index = parts.index("msg")
                    parts[raw_index], parts[msg_index] = parts[msg_index], parts[raw_index]
                    new_filename = "_".join(parts)
                    old_filepath = os.path.join(folder_name, filename)
                    new_filepath = os.path.join(folder_name, new_filename)
                    os.rename(old_filepath, new_filepath)
                    print(f"Zmieniono nazwę pliku: {old_filepath} -> {new_filepath}")

root_dir = "./results"
rename_files(root_dir)
