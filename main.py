from pytube import YouTube
from moviepy.editor import VideoFileClip


def downloadVideo(yt):
    audio_stream = yt.streams.filter(file_extension='mp4').first()
    download_path = "./downloadMP4"
    audio_stream.download(output_path=download_path)
    print("Download do vídeo concluído!")


def convertMp4ToMp3(yt):
    video_path = "./downloadMP4/" + yt.title + ".mp4"
    audio_path = "./downloadMP3/" + yt.title + ".mp3"
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    print("Conversão concluída!")


if __name__ == '__main__':
    url = input("URL do vídeo: ")
    yt = YouTube(url)

    print("Opção 0: sair")
    print("Opção 1: inserir nova url")
    print("Opção 2: fazer download do vídeo")
    print("Opção 3: converter vídeo em mp3")

    while True:
        option = input()
        option = int(option)
        if option == 0:
            print("Saindo do programa.")
            break
        elif option == 1:
            url = input("URL do vídeo: ")
            yt = YouTube(url)
        elif option == 2:
            downloadVideo(yt)
        elif option == 3:
            convertMp4ToMp3(yt)
        else:
            print("Opção inválida. Tente novamente.")

