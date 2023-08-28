"""This will send a cheque to a contact."""

import postgrid
import os

postgrid.pm_key = os.environ["POSTGRID_PM_API_KEY"]

to_contact = postgrid.Contact.create(
    first_name="John",
    last_name="Smith",
    address_line1="20-20 Bay St",
    address_line2="Floor 11",
    city="Toronto",
    province_or_state="ON",
    postal_or_zip="M5J 2N8",
    country_code="CA",
) 

from_contact = postgrid.Contact.create(
    first_name="Jane",
    last_name="Doe",
    address_line1="149 Sauve St",
    city="Montreal",
    province_or_state="QC",
    postal_or_zip="H9C 2Z7",
    country_code="CA",
)

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

pdf = open("assets/letter_8.5x11.pdf", "rb")

cheque = postgrid.Cheque.create(
    description='Cool new check', 
    to=to_contact.id, 
    from_=from_contact.id, 
    bank_account=bank.id, 
    amount=10000,
    memo='Invoice 1233',
    number=9667, 

    # This will attach a letter to the cheque
    # You may choose to omit this field
    letter_html='Hello {{to.firstName}}', 

    # You can also use letter_pdf instead,
    # see the examples for letters and postcards
    # letter_pdf=pdf,
    # Don't forget to remove letter_html if you use letter_pdf
)
