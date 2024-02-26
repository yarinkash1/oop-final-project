from Post import Post
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImagePost(Post):
    def __init__(self,image_file):
        super().__init__()
        self.__image_file=image_file

    def display(self):
        print("Shows picture")
        img=mpimg.imread(self.__image_file)
        imgplot = plt.imshow(img)
        plt.axis('off')
        plt.show()




    def __str__(self):
        str = f"{self.getUploadingUser().get_username()} posted a picture\n"
        return str