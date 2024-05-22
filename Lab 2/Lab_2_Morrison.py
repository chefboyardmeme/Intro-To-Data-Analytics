import random

class CreditCard:
    # Dictionary mapping card type key to card type name
    card_types = {1: 'Visa', 2: 'Master', 3: 'Amex', 4: 'Discover'}

    def __init__(self, card_number, card_owner, expiration_date):
        """
        Constructor method for CreditCard class.

        Parameters:
        - card_number: string representing the credit card number
        - card_owner: string representing the name of the card owner
        - expiration_date: string representing the expiration date of the credit card
        """
        # Initialize instance variables
        self.card_number = card_number
        self.card_owner = card_owner
        self.expiration_date = expiration_date
        self.credit_limit = 1000
        # Set initial balance to a random value below the credit limit
        self.balance = random.random() * self.credit_limit
        # Determine card type based on the card number
        self.card_type = self._get_card_type(card_number)

    def _get_card_type(self, card_number):
        """
        Private method to determine the card type based on the card number.

        Parameters:
        - card_number: string representing the credit card number

        Returns:
        - string representing the card type (or 'Not Supported Card Type' if not found)
        """
        card_type_key = int(card_number[5])
        return self.card_types.get(card_type_key, 'Not Supported Card Type')

    def get_cardOwner(self):
        """
        Getter method for retrieving the card owner's name.
        """
        return self.card_owner

    def set_cardOwner(self, card_owner):
        """
        Setter method for updating the card owner's name.

        Parameters:
        - card_owner: string representing the new name of the card owner
        """
        self.card_owner = card_owner

    def get_cardType(self):
        """
        Getter method for retrieving the card type.
        """
        return self.card_type

    def set_cardType(self, card_type):
        """
        Setter method for updating the card type.

        Parameters:
        - card_type: string representing the new card type
        """
        self.card_type = card_type

    def processOrder(self, transaction_amount):
        """
        Method to process a transaction order.

        Parameters:
        - transaction_amount: float representing the amount of the transaction

        Returns:
        - True if the transaction is successfully processed, False otherwise
        """
        # Check if the card type is supported and if the balance is sufficient
        if self.card_type == 'Not Supported Card Type' or transaction_amount > self.balance:
            return False
        # Deduct transaction amount from the balance
        self.balance -= transaction_amount
        return True

    def __str__(self):
        """
        Method to represent the CreditCard object as a string.

        Returns:
        - String representation of the CreditCard object
        """
        return f"{self.card_owner} is the owner of the credit card with number {self.card_number} which expires on {self.expiration_date}"
