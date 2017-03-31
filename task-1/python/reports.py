class TextReporter(object):
    
    @staticmethod
    def statement(customer):
        result = "Rental summary for %s\n" %customer.name
        total_dept = 0.0
        total_bonus = 0.0

        for rent in sorted(customer.rentals, key=lambda x: x.movie.title):
            
            cur_dept = rent.dept
            cur_bonus = rent.bonus
            
            total_dept += cur_dept
            total_bonus += cur_bonus

            result += "\t%s\t%s\n" %(rent.movie.title, cur_dept)
        
        result += "Total debt: %s\n" %total_dept
        result += "You earned %s points for your activity" %total_bonus
        
        print result
        
            
