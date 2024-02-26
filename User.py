import SocialNetwork
from PostFactory import PostFactory

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__is_online = False
        self.__followers = []
        self.__following = []
        self.__posts = []
        self.__notifications = []

    def get_username(self):
        return self.__username

    def set_status(self,status):
        self.__is_online=status

    def get_status(self):
        return self.__is_online

    def get_password(self):
        return self.__password


    def follow(self,followed_user):

        is_connected=False
        already_followed=False
        following_himself=True


        if(self.__is_online==True):
            is_connected=True


        j = 0
        for j in range(len(self.__following)):

            if(followed_user.__username == self.__following[j].__username):
                already_followed=True
                break


        if not(self.__username==followed_user.__username):
            following_himself=False


        if(is_connected==True and already_followed==False and following_himself==False):
            self.__following.append(followed_user)
            followed_user.__followers.append(self)
            print(self.__username + " started following " + followed_user.__username)

    def unfollow(self,unfollowed_user):

        is_connected=False
        already_unfollowed=True
        unfollowing_himself=False

        if(self.__is_online==True):

            is_connected=True


        j = 0
        for j in range(len(self.__following)):

            if(unfollowed_user.__username == self.__following[j].__username):
                already_unfollowed=False
                break


        if(self.__username==unfollowed_user.__username):
            unfollowing_himself=True


        if(is_connected==True and already_unfollowed==False and unfollowing_himself==False):
            self.__following.remove(unfollowed_user)
            unfollowed_user.__followers.remove(self)
            print(self.__username + " unfollowed " + unfollowed_user.__username)

    def publish_post(self, post_type, *args):
        if (self.__is_online == True):
            post_factory = PostFactory()
            post = PostFactory.create_post(post_type, *args)
            self.__posts.append(post)
            if(post_type=="Text"):
                print(f"{self.get_username()} published a post:\n\"{post.getString()}\"\n")
                post.setUploadingUser(self)
            if(post_type=="Image"):
                print(f"{self.get_username()} posted a picture\n")
                post.setUploadingUser(self)
            if (post_type == "Sale"):
                print(f"{self.get_username()} posted a product for sale:")
                print(f"for sale! {post.getItemDescription()}, price: {post.getPrice()}, pickup from: {post.getPickUpLocation()}\n")
                post.setUploadingUser(self)
            self.notify()
            return post

    def __str__(self):
        str=f"User name: {self.__username}, Number of posts: {len(self.__posts)}, Number of followers: {len(self.__followers)}"
        return str

    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    def add_notification(self, notification):
        self.__notifications.append(notification)

    def notify(self):
        for followers in self.__followers:
            followers.add_notification(self.get_username() + " has a new post")



