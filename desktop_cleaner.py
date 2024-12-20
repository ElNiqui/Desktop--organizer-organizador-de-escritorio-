import os
import shutil
import schedule
import time

# camino al escritorio
desktop_path = os.path.expanduser("C:\\Users\\nvici\\Desktop")

# Categorias de Archivos
file_categories = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Musica": [".mp3", ".wav", ".aac"],
    "Archivos": [".zip", ".rar", ".7z"],
    "Otros": []  
}

# Funcion para organizar los archivos
def organize_desktop():
    print("Organizing desktop...")
    
    # repetir en cada archivo
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # no modificar si es una carpeta
        if os.path.isdir(file_path):
            continue
        
        print(f"Processing: {filename}")  # Registrar el archivo actual

        # mover archivos basado en la extension 
        moved = False
        for category, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                category_folder = os.path.join(desktop_path, category)
                os.makedirs(category_folder, exist_ok=True)  
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}")  
                moved = True
                break
        
        # si el archivo no responde a ninguna categoria, moverlo a otros
        if not moved:
            otros_folder = os.path.join(desktop_path, "Otros")
            os.makedirs(otros_folder, exist_ok=True)  # Crear "otros" si no existe la carpeta
            shutil.move(file_path, os.path.join(otros_folder, filename))
            print(f"Moved {filename} to 'Otros'")  # registrar cuando el archivo es movido a otros 
    
    print("Escritorio organizado")

organize_desktop()

schedule.every().week.do(organize_desktop)

print("Se inicio el programador. Presione Ctrl+C para detenerlo.")
while True:
    schedule.run_pending()
    time.sleep(1)