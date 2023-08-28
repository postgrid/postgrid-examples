"""Gets the 10 most recent letters and prints their IDs and recipient."""

import postgrid
import os

postgrid.pm_key = os.environ["POSTGRID_PM_API_KEY"]

print("Showing 10 most recent letters:")
recent = postgrid.Letter.list(limit=10)
for letter in recent.data:
    print("Letter ID: " + letter.id)
    print("Sent to: " + letter.to.address_line1)
