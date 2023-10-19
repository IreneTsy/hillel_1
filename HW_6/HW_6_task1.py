suma = int(input('Enter the amount '))
term = int(input('Choose the term - 1 or 5 years '))
term_month = term*12
term_overall = term*12
print('|', 'Month'.center(3), '|',
      'Monthly payment'.center(3), '|',
      'Percent per month'.center(3),  '|',
     'Debt to pay', '|')
if term == 1 or term == 5:
    for term_month in range(1, term_month+1):
        if term_month <= 24:
            #percent = '2%'
            suma_per_month = (suma/term_overall)+(suma*0.02)
            perc_per_month = suma*0.02
            suma = suma - (suma/term_overall)
            term_overall = term_overall - 1 
            print('|',("%.0f"%term_month).center(len('Month')), '|',
          ("%.2f"%suma_per_month).ljust(len('Monthly payment')), '|',
          ("%.2f"%perc_per_month).ljust(len('Percent per month')), '|',
          ("%.2f"%suma).ljust(len('Debt to pay')), '|'.ljust(5))
        else:
            #percent = '4%'
            suma_per_month = (suma/term_overall)+(suma*0.04)
            perc_per_month = suma*0.04
            suma = suma - (suma/term_overall)
            term_overall = term_overall - 1
            print('|',("%.0f"%term_month).center(len('Month')), '|',
          ("%.2f"%suma_per_month).ljust(len('Monthly payment')), '|',
          ("%.2f"%perc_per_month).ljust(len('Percent per month')), '|',
          ("%.2f"%suma).ljust(len('Debt to pay')), '|'.ljust(5))