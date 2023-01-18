from pytube import YouTube


class YoutubeDownloader:

    def __init__(self) -> None:
        super().__init__()

    def download(self, url: str = 'https://www.youtube.com/watch?v=EsyUa63NM1E',
                 type_of_download: str = 'video') -> str:
        yt = YouTube(url)
        try:
            if type_of_download == 'audio':
                self.download_audio(yt)
                return 'Downloaded audio'
            self.download_video(url)
            return 'Downloaded video'
        except Exception as e:
            print(e)


    def download_video(self, yt: YouTube):
        resolution = self.find_appropriate_format(yt)
        yt.streams.get_by_resolution(resolution).download('./yt_videos')

    def find_appropriate_format(self, yt) -> str:
        formats = yt.streaming_data['formats']
        highest_res = ''
        for video_format in formats:
            if video_format['qualityLabel'] > highest_res:
                highest_res = video_format['qualityLabel']
        if highest_res == '240p':
            return '360p'
        return highest_res

    def download_audio(self, yt: YouTube):
        yt.streams.get_audio_only("mp4").download('./yt_audio')
