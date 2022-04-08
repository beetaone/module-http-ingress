""" Egress to the next module
"""
import json
import time

from app.config import APPLICATION, WEEVE
from requests import post


def send_data(data: json, timestamp=time.time()) -> bool:
    """Sends data to the next module

    Args:
        data (json): [description]
        timestamp ([float], optional): [description]. Defaults to time.time().

    Returns:
        bool: If the data was sent properly
    """

    try:
        headers = {}
        if APPLICATION['AUTHENTICATION_REQUIRED'] == 'yes' and APPLICATION['ACCESS_TOKEN'] != '':
            headers.update({"Authorization": f"{APPLICATION['ACCESS_TOKEN']}"})
        if APPLICATION['AUTHENTICATION_API_KEY'] != '':
            headers.update({'x-api-key': APPLICATION['AUTHENTICATION_API_KEY']})
        # URL Convetion 1
        if not WEEVE['EGRESS_URL']:
            resp = post(
                url=f"{WEEVE['EGRESS_SCHEME']}://{WEEVE['EGRESS_HOST']}:{WEEVE['EGRESS_PORT']}/{WEEVE['EGRESS_PATH']}",
                json=data,
                headers=headers,
            )
        # URL Convetion 2
        else:
            resp = post(url=f"{WEEVE['EGRESS_URL']}", json=data, headers=headers)

        # success = 200
        if resp.status_code == 200:
            return True
        # failure = 500
        else:
            return False
    except Exception:
        return False
