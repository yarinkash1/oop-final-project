from Post import Post


class TextPost(Post):
    def __init__(self,content_str):
        super().__init__()
        self.__content_str = content_str

    def getString(self):
        return self.__content_str

    def __str__(self):
        str = f"{self.getUploadingUser().get_username()} published a post: \n\"{self.__content_str}\"\n"
        return str

