"""This will send a letter to a contact using merge variables."""

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

template = postgrid.Template.create(
    description='Cool new template',
    html='<html><body>Here is your special code: {{userDetails.secret}}</body></html>',
)

letter = postgrid.Letter.create(
    description='Cool new letter with merge variables', 
    template=template.id,
    to=to_contact.id,
    from_=from_contact.id,
    merge_variables={
        'userDetails': {
            'secret': "42"
        }
    }
)
