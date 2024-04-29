import os
import pandas as pd

# Ścieżka do folderu z danymi
results_folder = "results/campus"

rosbag_name = "campus_2011_09_28_bag"

# Pusta lista do przechowywania danych z plików CSV
data_frames = []

# Pętla po plikach CSV w katalogu
for filename in os.listdir(results_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(results_folder, filename)
        
        # Wyodrębnienie nazwy metody z nazwy pliku
        method = os.path.splitext(filename)[0].split("_")[-1].capitalize()
        
        compresion_type = filename.split("_")[1]
        
        method = "Per Second" if method == "Data" else "Per Message"
        
        # Wczytanie danych z pliku CSV
        data = pd.read_csv(file_path)
        print(data.head())
        
        # Obliczenie średniej wartości bandwidth i odchylenia standardowego w Mb/s
        data["bandwidth_mbps"] = data["data"] / 1000000 # przeliczenie na megabajty
        average_bandwidth = data["bandwidth_mbps"].mean()
        std_dev_bandwidth = data["bandwidth_mbps"].std()
        
        # Dodanie wyników do listy jako słownik
        data_frames.append({"Rosbag": rosbag_name,
                            "Compression Type": compresion_type,
                            "Method": method,
                            "Average Bandwidth [Mb/s]": average_bandwidth,
                            "Standard Deviation": std_dev_bandwidth})

# Konwersja listy słowników do DataFrame
results_df = pd.DataFrame(data_frames)

# Posortowanie wyników po typie kompresji
results_df = results_df.sort_values(by="Compression Type")

# Zapisanie wyników do pliku CSV
output_file = os.path.join(results_folder, "summary_bandwidth_results.csv")
results_df.to_csv(output_file, index=False)
print(f"Saved summary results to {output_file}")
