class TextReporter(object):
    """
    Class for text report of customer rents preperation
    """
    @staticmethod
    def statement(customer):
        result = "Rental summary for %s\n" %customer.name
        total_dept = 0.0
        total_bonus = 0.0

        for rent in customer.rentals:

            cur_dept = rent.dept
            cur_bonus = rent.bonus

            total_dept += cur_dept
            total_bonus += cur_bonus

            result += "\t%s\t%s\n" %(rent.movie.title, cur_dept)

        result += "Total debt: %s\n" %total_dept
        result += "You earned %s points for your activity" %total_bonus

        print result


class HtmlReporter(object):
    """
    Class for html report of customer rents preperation
    """

    @staticmethod
    def statement(customer):

        customer_rentals = []
        total_bonus = 0

        for rent in sorted(customer.rentals,
                           key=lambda x: x.movie.title):

            total_bonus += rent.bonus
            customer_rentals.append((rent.movie.title, rent.dept))

        result = \
            """<!DOCTYPE HTML>\n<html>\n <head>\n  <meta charset="utf-8">
  <title>Rental summary for %s</title>\n </head>\n <body>\n  <table border="1">
   <caption>Rental summaty for %s</caption>\n   <caption>Total dept: %s</caption>
   <caption>You earned: %s</caption>\n   <tr>\n    <th>Title</th>\n    <th>Cost</th>
   </tr>\n""" %(
       customer.name, customer.name,
       sum([rent[1] for rent in customer_rentals]),
       total_bonus)

        for item in customer_rentals:
            result += "   <tr><td>%s</td><td>%s</td></tr>\n" %(
                item[0], item[1])

        result += "   </table>\n </body>\n</html>"

        print result
