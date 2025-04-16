from abc import ABC, abstractmethod

# Step 1: Abstract Component (Base Beverage)
class Beverage(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Step 2: Concrete Components (Specific Beverages)
class Espresso(Beverage):
    def get_description(self):
        return "Espresso"

    def get_cost(self):
        return 2.0


class Latte(Beverage):
    def get_description(self):
        return "Latte"

    def get_cost(self):
        return 3.0


# Step 3: Abstract Decorator
class AddOnDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description()

    def get_cost(self):
        return self.beverage.get_cost()


# Step 4: Concrete Decorators (Add-Ons)
class Milk(AddOnDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def get_cost(self):
        return self.beverage.get_cost() + 0.5


class Sugar(AddOnDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Sugar"

    def get_cost(self):
        return self.beverage.get_cost() + 0.2


class WhippedCream(AddOnDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Whipped Cream"

    def get_cost(self):
        return self.beverage.get_cost() + 0.7


# Step 5: Client Code
if __name__ == "__main__":
    # Order an Espresso
    beverage = Espresso()
    print(f"Order: {beverage.get_description()} | Cost: ${beverage.get_cost()}")

    # Add Milk to Espresso
    beverage = Milk(beverage)
    print(f"Order: {beverage.get_description()} | Cost: ${beverage.get_cost()}")

    # Add Sugar to Espresso with Milk
    beverage = Sugar(beverage)
    print(f"Order: {beverage.get_description()} | Cost: ${beverage.get_cost()}")

    # Order a Latte with Whipped Cream
    beverage2 = Latte()
    beverage2 = WhippedCream(beverage2)
    print(f"Order: {beverage2.get_description()} | Cost: ${beverage2.get_cost()}")