"""Showcasing webhook creation"""

import postgrid
import os

postgrid.pm_key = os.environ["POSTGRID_PM_API_KEY"]

webhook = postgrid.Webhook.create(
    enabled_events=['letter.created'], 
    url='https://my.service.com/postgrid/callback'
)
