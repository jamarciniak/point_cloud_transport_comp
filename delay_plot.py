import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ścieżka do folderu z danymi
results_folder = "results"

# Metody do porównania
methods = ["zlib", "draco", "zstd"]

# Pętla po kategoriach (campus, city, person, residential, road)
for category in os.listdir(results_folder):
    category_folder = os.path.join(results_folder, category)
    
    # Pętla po metodach
    for method in methods:
        # Wczytanie danych z plików CSV
        raw_file = os.path.join(category_folder, f"{category}_raw_bandwidth_data.csv")
        method_file = os.path.join(category_folder, f"{category}_{method}_bandwidth_data.csv")
        
        if os.path.exists(raw_file) and os.path.exists(method_file):
            raw_data = pd.read_csv(raw_file)
            method_data = pd.read_csv(method_file)
            print(method_data.head())
            # Złączenie danych na podstawie kolumny "timestamp"
            merged_data = pd.merge(raw_data, method_data, on="index", suffixes=('_raw', f'_{method}')).reset_index()
            
            # Wyświetlenie danych
            # print(f"\n{category.capitalize()} - {method.capitalize()} Bandwidth Comparison:")
            # print("Index\tTimestamp\t\t\tRaw Data\t", f"{method.capitalize()} Data")
            # print(merged_data.head(10))
            # for idx, row in merged_data.iterrows():
                # print(f"{row['index']}\t{row['timestamp']}\t{row['data_raw']}\t{row[f'data_{method}']}")
            
            # Wykres opóźnień
            plt.figure(figsize=(10, 6))
            # plt.plot(np.array(merged_data['index']), np.array(merged_data[f'timestamp_raw']), label='Raw Data')
            plt.plot(np.array(merged_data['index']), (np.array(merged_data[f'timestamp_{method}'])-np.array(merged_data['timestamp_raw'])), label=f'{method.capitalize()} timestamp difference')
            plt.xlabel('index')
            plt.ylabel('timestamp diff')
            plt.title(f'{category.capitalize()} - {method.capitalize()} Bandwidth Comparison')
            plt.savefig(f"{category_folder}/{category}_{method}_bandwidth_comparison.png")
