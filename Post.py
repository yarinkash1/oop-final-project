class Post:
    def __init__(self,*args):
        self.__likes=[]
        self.__comments =[]
        self.__uploading_user=None


    def setUploadingUser(self,uploading_user):
        self.__uploading_user=uploading_user


    def getUploadingUser(self):
        return self.__uploading_user


    def like(self,User):
        if(User not in self.__likes and User.get_status==True):
          self.__likes.append(User)
        if(User!=self.__uploading_user):
            notification_str = f"{User.get_username()} liked your post"
            self.__uploading_user.add_notification(notification_str)
            print(f"notification to {self.getUploadingUser().get_username()}: " + notification_str)


    def likes(self):
       return len(self.__likes)


    def comment(self,User,cmnt):
        if(User.get_status == True):
           self.__comments.append(cmnt)
        if (User != self.__uploading_user):
            notification_str = f"{User.get_username()} commented on your post"
            self.__uploading_user.add_notification(notification_str)
            print(f"notification to {self.getUploadingUser().get_username()}: " + notification_str + ": " + cmnt)








