import os

def rename_files(root_dir):
    for folder_name, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".csv"):
                parts = filename.split("_")
                if len(parts) >= 4 and "raw" in parts and "msg" in parts:
                    raw_index = parts.index("raw")
                    msg_index = parts.index("msg")
                    prefix = parts[0]
                    suffix = "_".join(parts[3:]).replace(".csv", "")
                    new_filename = f"{prefix}_{'_'.join(parts[raw_index + 1:msg_index])}_{'_'.join(parts[msg_index + 1:raw_index])}_{suffix}.csv"
                    old_filepath = os.path.join(folder_name, filename)
                    new_filepath = os.path.join(folder_name, new_filename)
                    os.rename(old_filepath, new_filepath)
                    print(f"Zmieniono nazwę pliku: {old_filepath} -> {new_filepath}")

root_dir = "./results"
rename_files(root_dir)
