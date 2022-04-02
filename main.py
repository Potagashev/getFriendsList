import requests

from constants import (
    TOKEN, USER_ID,
    KEYS, TITLES,
    VALID_OUTPUT_TYPES,
    OUTPUT_PATH,
    OUTPUT_TYPE,
    ORDER, URL,
    FIELDS, V,
)
from report_maker import ReportMaker
from utils import format_data


def main():
    # если в пути указывается формат, система его игнорирует
    output_path = ""
    if (OUTPUT_PATH.split('.'))[-1] in VALID_OUTPUT_TYPES:
        output_path = "".join(OUTPUT_PATH.split('.')[:-1])
    output_type = OUTPUT_TYPE.lower()

    request = f"{URL}?"\
                f"v={V}&"\
                f"access_token={TOKEN}&"\
                f"user_id={USER_ID}&"\
                f"fields={FIELDS}&"\
                f"order={ORDER}"

    response = requests.get(request)

    # обработка ошибок
    try:
        data = response.json()['response']['items']
    except KeyError:
        print('\033[31mERROR: ' + response.json()['error']['error_msg'])
        return

    new_data = format_data(data)

    print(new_data)

    report_maker = ReportMaker()
    report_maker.make_report(
        data=new_data,
        format=output_type,
        output_path=f"{output_path}.{output_type}"
    )


if __name__ == "__main__":
    main()
