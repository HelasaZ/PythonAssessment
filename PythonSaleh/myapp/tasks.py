from celery import shared_task
from .models import Mcom
import requests
from datetime import datetime

@shared_task
def sync_data_periodically():
    apiKey = " API KEY HERE !!"
    apiUrl = "https://api.monday.com/v2"
    headers = {"Authorization": apiKey}

    query = '{ items (ids: 1275365816) { id name column_values { title text }} }'  # recup les ids des items du grp + chaque elem des items

    data = {'query': query}

    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    api_data = r.json()['data']['items']

    # Supprimez les données existantes dans la base de données
    Mcom.objects.all().delete()

    # Enregistrez les nouvelles données dans la base de données
    for item_data in api_data:
        mcom = Mcom(
            guest_name=item_data['name'],
            status=item_data['column_values'][1]['text'],
            flat_booked=item_data['column_values'][8]['text'],
            checkin_date=datetime.strptime(item_data['column_values'][5]['text'].split(' - ')[0], '%Y-%m-%d').date(),
            checkout_date=datetime.strptime(item_data['column_values'][5]['text'].split(' - ')[1], '%Y-%m-%d').date(),
            creation_log=datetime.strptime(item_data['column_values'][25]['text'], '%Y-%m-%d %H:%M:%S UTC'),
            booking_value=item_data['column_values'][11]['text']
        )
        mcom.save()
