import sys
from pprint import pprint

import requests

import constants
from report_maker import ReportMaker
from utils import format_date_to_iso, format_data


def get_friends(
        access_token: str,
        user_id: int,
        format=constants.OUTPUT_TYPE,
        output_path=f'report.{constants.OUTPUT_TYPE}'):
    format = format.lower()

    response = requests.get(f"{constants.URL}?"
                            f"v={constants.V}&"
                            f"access_token={access_token}&"
                            f"user_id={user_id}&"
                            f"fields={constants.FIELDS}&"
                            f"order={constants.ORDER}")

    # обработка ошибок
    try:
        data = response.json()['response']['items']
    except KeyError:
        print('\033[31mERROR: ' + response.json()['error']['error_msg'])
        return

    new_data = format_data(data)

    print(new_data)

    report_maker = ReportMaker()
    report_maker.make_report(data=new_data,
                             format=format,
                             output_path=output_path
                             )


get_friends(access_token='cd1bbea8d225d0b4ecf8f5550be363b1f55e9fdffc1cee652ecf25639cf7f4aacdb7144649f9bbf1ce306',
            user_id=222622761,
            format='csv',
            output_path='report.json'
            )

# get_friends(access_token=constants.TOKEN,
#             user_id=constants.USER_ID,
#             format=constants.OUTPUT_TYPE,
#             output_path=constants.OUTPUT_PATH)

# get_friends(
#     access_token=sys.argv[1],
#     user_id=int(sys.argv[2]),
#     format=sys.argv[3],
#     output_path=sys.argv[4])


