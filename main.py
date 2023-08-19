import os
import argparse


def delete_crached_vessels(folder_path: str) -> None:
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            contains_crached = any("splashed = True" in line for line in lines)
            
            if contains_crached:
                os.remove(file_path)
                print(f"Fichier {filename} supprimé.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Supprimer les fichiers qui contiennent 'crached = True'.")
    parser.add_argument("folder_path", type=str, help="Chemin vers le dossier à traiter.")
    args = parser.parse_args()
    delete_crached_vessels(args.folder_path)
