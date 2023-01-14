from pytube import YouTube


class YoutubeDownloader:

    def __init__(self) -> None:
        super().__init__()

    def download(self, url: str = 'https://www.youtube.com/watch?v=EsyUa63NM1E',
                 type_of_download: str = 'video') -> str:
        if type_of_download == 'video':
            self.download_video(url)
            return 'video'
        self.download_audio(url)
        return 'audio'

    def download_video(self, url: str):
        yt = YouTube(url)
        try:
            resolution = self.find_appropriate_format(yt)
            yt.streams.get_by_resolution(resolution).download('./yt_videos')
        except Exception as e:
            print(e)

    def find_appropriate_format(self, yt) -> str:
        formats = yt.streaming_data['formats']
        highest_res = ''
        for video_format in formats:
            if video_format['qualityLabel'] > highest_res:
                highest_res = video_format['qualityLabel']
        if highest_res == '240p':
            return '360p'
        return highest_res

    def download_audio(self, url: str):
        pass
