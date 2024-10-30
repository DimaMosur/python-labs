class Clip:
    number_of_comments = 0
    category = "Music"

    def __init__(self, artist_name="", song_title="", duration=0, views=0):
        self.__artist_name = artist_name
        self.__song_title = song_title
        self.__duration = duration
        self.__views = views

    def get_artist_name(self):
        return self.__artist_name

    def set_artist_name(self, artist_name):
        self.__artist_name = artist_name

    def get_song_title(self):
        return self.__song_title

    def set_song_title(self, song_title):
        self.__song_title = song_title

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        current_artist_name = self.get_artist_name()
        self.__duration = duration

    def get_views(self):
        return self.__views

    def set_views(self, views):
        self.__views = views

    def __str__(self):
        return f"Clip: {self.__artist_name} - {self.__song_title} ({self.__duration} seconds, {self.__views} views)"

    def __repr__(self):
        return f"Clip(artist_name='{self.__artist_name}', song_title='{self.__song_title}', duration={self.__duration}, views={self.__views})"

    def __del__(self):
        print(f"Clip '{self.__artist_name} - {self.__song_title}' is being deleted")

def main():
    clip1 = Clip("Artist1", "Song1", 210, 50000)
    clip2 = Clip("Artist2", "Song2", 180, 150000)
    clip3 = Clip("Artist3", "Song3", 240, 30000)

    print(clip1)
    print(clip2)
    print(clip3)

    print(repr(clip1))
    print(repr(clip2))
    print(repr(clip3))
    clip1.set_artist_name("New Artist1")
    print(f"Updated artist of clip1: {clip1.get_artist_name()}")

main()
