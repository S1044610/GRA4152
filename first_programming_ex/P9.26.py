## A Customer class to handle a customer loyalty marketing campaign. After accumulating $100 in purchases, 
# the customer receives a $10 discount on the next purchase. 
#
class Customer:
    ## Constructs a customer with total purchase amount of 0.
    #
    def __init__(self):
        self._total_purchase = 0
        self._discount = False

    ## Get the amount of a purchase completed by the customer.
    # @param amount the amount of the purchase
    #
    def makePurchase(self, amount):
        if self._discount:
            amount = amount - 10 if amount >= 10 else 0
            self._discount = False

        self._total_purchase += amount
        
        if self._total_purchase >= 100:
            self._discount = True
            self._total_purchase -= 100

    ## Gets the customer  reached the discount or not.
    # @return True if the customer get the discount
    #
    def discountReached(self):
        return self._discount

# Test class
if __name__ == "__main__":
    customer = Customer()
    customer.makePurchase(100)
    print(customer.discountReached()) # True, get a discount

    customer.makePurchase(95)
    print(customer.discountReached()) # False

    customer.makePurchase(50)
    print(customer.discountReached()) # True
