from pprint import pprint

import constants

import requests

from report_maker import ReportMaker


def get_friends(access_token: str, user_id: int, format='JSON', output_path=f'report.{constants.OUTPUT_TYPE}'):
    format = format.upper()
    url = 'https://api.vk.com/method/friends.get'
    v = '5.131'
    fields = 'country, city, bdate, sex'
    order = 'name'
    response = requests.get(f"{url}?"
                            f"v={v}&"
                            f"access_token={access_token}&"
                            f"user_id={user_id}&"
                            f"fields={fields}&"
                            f"order={order}")

    report_maker = ReportMaker()
    data = response.json()['response']['items']
    new_data = []
    for i in range(len(data)):
        new_data.append({
            field: data[i].get(field) for field in constants.KEYS
        })
    report_maker.make_report(data=new_data, headers=constants.KEYS, format=format, outputpath_path=output_path)


pprint(get_friends(
    access_token='5bbc3862bf2f8cbb3cded0072e936d8dad1722e8f83134c50819ac615d4e469ff26afb151b9f2eb3e1a8d',
    user_id=222622761,
    format='JSON'))

