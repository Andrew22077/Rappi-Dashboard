import pandas as pd
import glob
import os

# Ruta donde están los CSV
files = glob.glob("data/data_cruda/*.csv")

all_data = []

print(f"Se encontraron {len(files)} archivos")
print("Iniciando procesamiento...\n")

for i, file in enumerate(files, start=1):
    print(f"Procesando archivo {i} de {len(files)}: {os.path.basename(file)}")

    df = pd.read_csv(file)
    
    # Convertir formato horizontal a vertical
    df_long = df.melt(
        id_vars=["Plot name", "metric (sf_metric)", "Value Prefix", "Value Suffix"],
        var_name="timestamp",
        value_name="value"
    )
    
    all_data.append(df_long)

print("\nUnificando todos los archivos...")

# Unir todos los archivos en uno solo
final_df = pd.concat(all_data, ignore_index=True)

# Guardarlo limpio
final_df.to_csv("dataset_unificado.csv", index=False)
final_df = final_df.drop_duplicates()

print("✅ Proceso terminado. Archivo guardado como dataset_unificado.csv")
