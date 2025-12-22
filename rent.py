

class Rent:
    def __init__(self, rent, food, member, electricity):
        self.rent = rent
        self.food = food
        self.member = member
        self.electricity = electricity

    def check_valid_input(self, value, expected_type, field_name):
        """Generic validation function for all inputs"""
        # Validate type first to avoid runtime errors when comparing
        if not isinstance(value, expected_type):
            print(f"Invalid input. Please enter a positive {expected_type.__name__} for {field_name}.")
            return False

        # Now it's safe to perform numeric comparisons
        if value <= 0:
            print(f"{field_name} must be a positive {expected_type.__name__}. Please try again.")
            return False

        return True


    def member_input(self):
        try:
            self.member = int(input("Enter the count of member: "))
            if self.check_valid_input(self.member, int, "Member count"):
                return self.member
            else:
                return self.member_input()
        except ValueError:
            print("Invalid input. Please enter a positive integer for member count.")
            return self.member_input() 
            
    # rent input and verification. 
    def input_rent(self):
        try:
            self.rent = int(input("Enter the amount of rent: "))
            if self.check_valid_input(self.rent, int, "Rent"):
                return self.rent
            else:
                return self.input_rent()
        except ValueError:
            print("Invalid input. Please enter a positive integer for rent.")
            return self.input_rent()

    def input_food(self):
        try:
            self.food = int(input("Enter the amount of food: "))
            if self.check_valid_input(self.food, int, "Food amount"):
                return self.food
            else:
                return self.input_food()
        except ValueError:
            print("Invalid input. Please enter a positive integer for food amount.")
            return self.input_food()   



    def Electricity_input(self):
        try:
            self.electricity = float(input("Enter the Units of Electricity: "))
            if self.check_valid_input(self.electricity, float, "Electricity amount"):
                return self.electricity
            else:
                return self.Electricity_input()
        except ValueError:
            print("Invalid input. Please enter a positive float for Electricity amount.")
            return self.Electricity_input()



    def calculate_total(self):
        total_bill = self.electricity * 10  # Assuming a fixed charge per unit
        # Use float division so each member can pay fractional amounts
        total = (self.rent + self.food + total_bill) / self.member
        return round(total, 2)
        




if __name__ == "__main__":    
    rent_instance = Rent(0, 0, 0, 0.0)
    rent_instance.input_rent()
    rent_instance.input_food()
    rent_instance.member_input()
    rent_instance.Electricity_input()
    total_per_member = rent_instance.calculate_total()
    print(f"Each member has to pay: {total_per_member}")




