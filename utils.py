import constants


def format_date_to_iso(date: str) -> str:
    date = date.split('.')
    formatted_date = ""

    for i in range(len(date)):
        if len(date[i]) == 1:
            date[i] = '0' + date[i]

    if len(date) == 3:
        formatted_date = f'{date[2]}-{date[1]}-{date[0]}'

    elif len(date) == 2:
        formatted_date = f'{date[1]}-{date[0]}'

    return formatted_date


def format_data(data: list) -> list:
    new_data = []
    for i in range(len(data)):
        dic = {}
        for key in constants.KEYS:
            dic[key] = data[i].get(key)
            if dic[key] is not None:
                # форматирование данных
                if key == 'country':
                    dic[key] = dic[key]['title']
                if key == 'city':
                    dic[key] = dic[key]['title']
                if key == 'bdate':
                    dic[key] = format_date_to_iso(dic[key])
                if key == 'sex':
                    if dic[key] == 1:
                        dic[key] = 'Женщина'
                    if dic[key] == 2:
                        dic[key] = 'Мужчина'

        new_data.append(dic)
    return new_data
