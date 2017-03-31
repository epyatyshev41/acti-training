from customer import Customer
from movies import RegularMovie, NewReleaseMovie, ChildrensMovie
from rental import RentalWithBonuses
from pricing import SimplePricingSystem
from bonuse import SimpleBonus
from reports import TextReporter

def main():
    
    cust = Customer("Customer1")

    curent_pricing = SimplePricingSystem()
    curent_bonuces = [SimpleBonus()]

    cust.add_rental(
        RentalWithBonuses(
            ChildrensMovie("Nightmare on Elm Street"),
            3, curent_pricing, curent_bonuces))
    
    cust.add_rental(
        RentalWithBonuses(
            RegularMovie("The Pirates of Caribbean"),
            1, curent_pricing, curent_bonuces))
    
    cust.add_rental(
        RentalWithBonuses(
            NewReleaseMovie("Kill Bill"),
            5, curent_pricing, curent_bonuces))
    
    reporter = TextReporter()
    reporter.statement(cust)
    
if __name__ == '__main__':
    main()
