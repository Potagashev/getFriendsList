import requests

from constants import (
    TOKEN, USER_ID,
    VALID_OUTPUT_FORMATS,
    OUTPUT_PATH,
    OUTPUT_FORMAT,
    ORDER, URL,
    FIELDS, V,
    MAX_COUNT
)
from report_maker import ReportMaker
from utils import format_data

# если в пути указывается формат, система его игнорирует
output_path = OUTPUT_PATH
if (OUTPUT_PATH.split('.'))[-1] in VALID_OUTPUT_FORMATS:
    output_path = "".join(OUTPUT_PATH.split('.')[:-1])
output_format = OUTPUT_FORMAT.lower()


def do_request_and_make_report(offset, page=1):
    request = f"{URL}?" \
              f"v={V}&" \
              f"access_token={TOKEN}&" \
              f"user_id={USER_ID}&" \
              f"fields={FIELDS}&" \
              f"order={ORDER}&" \
              f"count={MAX_COUNT}&" \
              f"offset={offset}"

    response = requests.get(request)

    # обработка ошибок
    try:
        data = response.json()['response']
    except KeyError:
        print('\033[31mERROR: ' + response.json()['error']['error_msg'])
        return

    friends_list = data['items']
    new_friends_list = format_data(friends_list)

    report_maker = ReportMaker()
    report_maker.make_report(
        data=new_friends_list,
        format=output_format,
        output_path=f"{output_path}_page{page}.{output_format}"
    )
    return data['count']


def main():
    """
    Делаем запрос, сразу достаем количество друзей,
    если все друзья не влазят в отчет, делаем еще отчеты.
    Делается так, чтобы не делать лишний запрос
    """
    friends_count = do_request_and_make_report(offset=0, page=1)

    if MAX_COUNT < friends_count:
        for i in range(1, friends_count // MAX_COUNT + 1):
            do_request_and_make_report(offset=MAX_COUNT*i, page=i+1)


if __name__ == "__main__":
    main()
