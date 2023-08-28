"""Managing bank accounts"""

import postgrid
import os

postgrid.pm_key = os.environ["POSTGRID_PM_API_KEY"]

bank = postgrid.BankAccount.create(  
    description='This is where to put your marshmallows',
    bank_name='Bank of Marshmallows',
    bank_primary_line='3288 Tara Lane',
    bank_secondary_line='Indianapolis, IN',
    bank_country_code='US',
    routing_number='123456789',
    account_number='100010001001',
    signature_text='Stay Puff'
)

print("Printing first 10 bank accounts:")
for bank in postgrid.BankAccount.list().data:
    print(bank.bank_name)
