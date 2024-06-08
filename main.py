class MusikAlbum:
    def __init__(self, executor: str, title: str):
        self.title = title
        self.executor = executor
        self.songs = []

    def add_song(self, song: str):
        self.songs.append(song)

    def remove_song(self, song: str):
        if song in self.songs:
            self.songs.remove(song)
    def change_executor_title(self,new_executor: str):
        self.executor = new_executor

    def change_album_title(self, new_title: str):
        self.title = new_title

    def get_change_status(self):
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True


class MusikCollection:
    def __init__(self, title: str):
        self.title = title
        self.albums = []


    def list_album(self):
        if album in self. albums:
            self.albums.len()

    def add_album(self, album: str):
        self.albums.append(album)

    def remove_albums(self, album: str):
        if album in self.albums:
            self.albums.remove(album)

    def get_change_status(self):
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True


musikalbum = MusikAlbum("что-то", "что- то2")
musikalbum.add_song('song10')
musikalbum.add_song('song16')
musikalbum.remove_song('song10')
album = MusikCollection
