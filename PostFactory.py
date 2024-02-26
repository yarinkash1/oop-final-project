
from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import  SalePost

class PostFactory:
    @staticmethod
    def create_post(post_type, *args):
        if post_type == "Text":
            return TextPost(*args)
        elif post_type == "Image":
            return ImagePost(*args)
        elif post_type == "Sale":
            return SalePost(*args)
        else:
            raise ValueError(f"Invalid post type: {post_type}")
