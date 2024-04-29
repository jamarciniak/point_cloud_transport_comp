# import matplotlib.pyplot as plt
# import numpy as np
# import sys
# import os.path

# path = sys.argv[1]
# suffix = sys.argv[2]
# print(suffix)
# print(path)
# suffix="_campus"
# filename_raw = f'bandwidth_data{suffix}.csv'
# filename_draco = f'bandwidth_data_draco{suffix}.csv'
# filename_zstd = f'bandwidth_data_zstd{suffix}.csv'
# filename_zlib = f'bandwidth_data_zlib{suffix}.csv'

# raw = np.genfromtxt(os.path.join(path,filename_raw), delimiter=',', skip_header=1, names=['timestamp', 'data', 'index'])
# draco = np.genfromtxt(os.path.join(path,filename_draco), delimiter=',', skip_header=1, names=['timestamp', 'data', 'index'])
# zstd = np.genfromtxt(os.path.join(path,filename_zstd), delimiter=',', skip_header=1, names=['timestamp', 'data', 'index'])
# zlib = np.genfromtxt(os.path.join(path,filename_zlib), delimiter=',', skip_header=1, names=['timestamp', 'data', 'index'])

# plt.plot(raw['index'], raw['data']/1e6)  # Convert to MB/s
# plt.plot(draco['index'], draco['data']/1e6)  # Convert to MB/s
# plt.plot(zstd['index'], zstd['data']/1e6)  # Convert to MB/s
# plt.plot(zlib['index'], zlib['data']/1e6)  # Convert to MB/s
# plt.legend(['Raw', 'Draco', 'Zstd', 'Zlib'])
# plt.xlabel('Time')
# plt.ylabel('Bandwidth (MBytes/s)')
# plt.title('Bandwidth over time')
# plt.savefig(f'results/bandwidth_plot{suffix}.png')


# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# def generate_plots(root_dir, output_dir):
#     # Przechodzenie przez każdy plik w drzewie katalogów
#     for root, dirs, files in os.walk(root_dir):
#         for file in files:
#             if file.endswith(".csv"):
#                 file_path = os.path.join(root, file)
#                 # Wczytywanie danych z pliku CSV
#                 try:
#                     df = pd.read_csv(file_path)
#                 except Exception as e:
#                     print(f"Nie można wczytać pliku {file_path}: {e}")
#                     continue
                
#                 # Generowanie wykresu
#                 plt.figure(figsize=(8, 6))
#                 plt.plot(np.array(df['index']), np.array(df['data'])/1e6)  # Convert to MB/s
#                 plt.legend()
#                 plt.xlabel('Time')
#                 plt.ylabel('Bandwidth (MBytes/s)')
#                 plt.title(f'Bandwidth over time - {file_path}')
                
#                 # Sprawdzenie i utworzenie katalogu wyjściowego, jeśli nie istnieje
#                 if not os.path.exists(output_dir):
#                     os.makedirs(output_dir)
                
#                 # Zapisywanie wykresu do pliku w katalogu wyjściowym
#                 output_file_path = os.path.join(output_dir, f"{file.split('.')[0]}.png")
#                 plt.savefig(output_file_path)
#                 plt.close()
#                 print(f"Zapisano wykres do {output_file_path}")

# # Wczytanie danych z katalogu "input" i generowanie wykresów do katalogu "output"
# input_dir = "./results/campus"
# output_dir = "./results/campus/plots"

# generate_plots(input_dir, output_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# def generate_common_plots(root_dir, output_dir):
#     # Inicjalizacja pustych list dla danych "bandwidth_per_msg" i "bandwidth_data"
#     bandwidth_per_msg_data = []
#     bandwidth_data = []
    
#     # Przechodzenie przez każdy plik w drzewie katalogów
#     for root, dirs, files in os.walk(root_dir):
#         for file in files:
#             if file.endswith(".csv"):
#                 file_path = os.path.join(root, file)
#                 # Wczytywanie danych z pliku CSV
#                 try:
#                     df = pd.read_csv(file_path)
#                     df.name = os.path.basename(file_path)  # Przypisanie nazwy pliku jako atrybutu "name" dla DataFrame
#                 except Exception as e:
#                     print(f"Nie można wczytać pliku {file_path}: {e}")
#                     continue
                
#                 # Rozdzielanie danych na "bandwidth_per_msg" i "bandwidth_data"
#                 if "bandwidth_per_msg" in file:
#                     bandwidth_per_msg_data.append(df)
#                 elif "bandwidth_data" in file:
#                     bandwidth_data.append(df)

#     # Tworzenie wspólnego wykresu dla danych "bandwidth_per_msg"
#     if bandwidth_per_msg_data:
#         plt.figure(figsize=(8, 6))
#         plt.title("Bandwidth per Message")
#         plt.xlabel("Time")
#         plt.ylabel("Bandwidth (MBytes/s)")
#         for df in bandwidth_per_msg_data:
#             legend_label = df.name.split('_')[-2]
#             plt.plot(np.array(df['index']), np.array(df['data'])/1e6, label=legend_label)  # Convert to MB/s
#         plt.legend()
#         plt.savefig(os.path.join(output_dir, "bandwidth_per_msg_common_plot.png"))
#         plt.close()
#         print(f"Zapisano wspólny wykres dla danych bandwidth_per_msg")

#     # Tworzenie wspólnego wykresu dla danych "bandwidth_data"
#     if bandwidth_data:
#         plt.figure(figsize=(8, 6))
#         plt.title("Bandwidth Data")
#         plt.xlabel("Time")
#         plt.ylabel("Bandwidth (MBytes/s)")
#         for df in bandwidth_data:
#             legend_label = df.name.split('_')[-2]
#             plt.plot(np.array(df['index']), np.array(df['data'])/1e6, label=legend_label)  # Convert to MB/s
#         plt.legend()
#         plt.savefig(os.path.join(output_dir, "bandwidth_data_common_plot.png"))
#         plt.close()
#         print(f"Zapisano wspólny wykres dla danych bandwidth_data")


# # Wczytanie danych z katalogu "input" i generowanie wspólnych wykresów do katalogu "output"
# input_dir = "./results/campus"
# output_dir = "./results/campus/plots"

# generate_common_plots(input_dir, output_dir)


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_common_plots(root_dir, output_dir, dataset_name):
    # Inicjalizacja pustych list dla danych "bandwidth_per_msg" i "bandwidth_data"
    bandwidth_per_msg_data = []
    bandwidth_data = []
    
    # Przechodzenie przez każdy plik w drzewie katalogów
    for root, dirs, files in os.walk(root_dir):
        for file in sorted(files):  # Sortowanie plików po nazwie
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                # Wczytywanie danych z pliku CSV
                try:
                    df = pd.read_csv(file_path)
                    df.name = os.path.basename(file_path)  # Przypisanie nazwy pliku jako atrybutu "name" dla DataFrame
                except Exception as e:
                    print(f"Nie można wczytać pliku {file_path}: {e}")
                    continue
                
                # Rozdzielanie danych na "bandwidth_per_msg" i "bandwidth_data"
                if "bandwidth_per_msg" in file:
                    bandwidth_per_msg_data.append(df)
                elif "bandwidth_data" in file:
                    bandwidth_data.append(df)

    # Tworzenie wspólnego wykresu dla danych "bandwidth_per_msg"
    if bandwidth_per_msg_data:
        plt.figure(figsize=(8, 6))
        plt.title(f"Bandwidth per Message - {dataset_name}")
        plt.xlabel("Time")
        plt.ylabel("Bandwidth (MBytes/s)")
        for df in bandwidth_per_msg_data:
            legend_label = df.name.split('_')[1]
            plt.plot(np.array(df['index']), np.array(df['data'])/1e6, label=legend_label)  # Convert to MB/s
        plt.legend()
        plt.savefig(os.path.join(output_dir, "bandwidth_per_msg_common_plot.png"))
        plt.close()
        print(f"Zapisano wspólny wykres dla danych bandwidth_per_msg")

    # Tworzenie wspólnego wykresu dla danych "bandwidth_data"
    if bandwidth_data:
        plt.figure(figsize=(8, 6))
        plt.title(f"Bandwidth per Second - {dataset_name}")
        plt.xlabel("Time")
        plt.ylabel("Bandwidth (MBytes/s)")
        for df in bandwidth_data:
            legend_label = df.name.split('_')[1]
            plt.plot(np.array(df['index']), np.array(df['data'])/1e6, label=legend_label)  # Convert to MB/s
        plt.legend()
        plt.savefig(os.path.join(output_dir, "bandwidth_data_common_plot.png"))
        plt.close()
        print(f"Zapisano wspólny wykres dla danych bandwidth_data")


# Wczytanie danych z katalogu "input" i generowanie wspólnych wykresów do katalogu "output"
input_dir = "./results/road"
output_dir = "./results/road"
dataset_name = "road_2011_09_26_bag"

generate_common_plots(input_dir, output_dir, dataset_name)
