"""This will send a postcard to a contact from a PDF URL."""

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

pdf = open("assets/postcard_6x4.pdf", "rb")

postcard = postgrid.Postcard.create(
    description='Cool new postcard', 
    pdf=pdf, # This can be replaced with a URL to a PDF
    to=to_contact.id,
    from_=from_contact.id,
    size="6x4",
)
