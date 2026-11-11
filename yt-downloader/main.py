import yt_dlp

def descargar_video(url_video):
    # Configuramos las opciones de descarga
    opciones = {
        # 'bestvideo+bestaudio/best' descarga la mejor calidad de video y audio disponible
        'format': 'bestvideo+bestaudio/best',
        # Guarda el archivo con el título del video en la carpeta actual
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    print("Iniciando la descarga... Por favor espera.")
    
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url_video])
        print("¡Descarga completada con éxito!")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    enlace = input("Introduce la URL del video de YouTube: ")
    descargar_video(enlace)
