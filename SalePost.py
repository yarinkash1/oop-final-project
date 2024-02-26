import User
from Post import Post

class SalePost(Post):
    def __init__(self,item_description,price,pickup_location):
        super().__init__()
        self.__item_description=item_description
        self.__price=price
        self.__pickup_location=pickup_location
        self.__availability=True

    def getItemDescription(self):
        return self.__item_description

    def getPrice(self):
        return self.__price

    def getPickUpLocation(self):
        return self.__pickup_location

    def getAvailability(self):
        return self.__availability

    def sold(self,password):
        if(self.getUploadingUser().get_password()==password):
            self.__availability=False
            print(f"{self.getUploadingUser().get_username()}'s product is sold")

    def discount(self,discount_percentage,password):
        if(self.getUploadingUser().get_password()==password and self.__availability==True):
            self.__price = self.__price - ((discount_percentage*self.__price)/100)
            print(f"disount on {self.getUploadingUser().get_username()} product! the new price is: {self.__price}")

    def __str__(self):
        if(self.__availability==True):
            product_available=f"{self.getUploadingUser().get_username()} posted a product for sale:\nfor sale! {self.getItemDescription()}, price: {self.getPrice()}, pickup from: {self.getPickUpLocation()}\n"
            return product_available
        else:
            product_not_available=f"{self.getUploadingUser().get_username()} posted a product for sale:\nsold! {self.getItemDescription()}, price: {self.getPrice()}, pickup from: {self.getPickUpLocation()}\n"
            return product_not_available




