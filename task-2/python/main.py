from store.bonus import SimpleBonus
from store.customer import Customer
from store.movies import RegularMovie, NewReleaseMovie, ChildrensMovie
from store.pricing import SimplePricingSystem
from store.rental import RentalWithBonuses
from store.reports import TextReporter, HtmlReporter

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

    text_reporter = TextReporter()
    text_reporter.statement(cust)

    html_reporter = HtmlReporter()
    html_reporter.statement(cust)

if __name__ == '__main__':
    main()
