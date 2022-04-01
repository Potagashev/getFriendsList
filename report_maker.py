import csv
import json
import constants

headers = constants.TITLES


def _dict_to_json(data, output_path=f'{constants.OUTPUT_PATH}.json'):
    # output_path = set_extension('json', output_path)
    string = json.dumps(data, ensure_ascii=False, indent=4)
    json_file = open(output_path, "w", encoding="utf-8")
    json_file.write(string)
    json_file.close()


def _dict_to_csv(data, output_path=f'{constants.OUTPUT_PATH}.csv'):
    with open(output_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(headers)
        for user in data:
            writer.writerow(user.values())


def _dict_to_tsv(data, output_path=f'{constants.OUTPUT_PATH}.tsv'):
    with open(output_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(headers)
        for user in data:
            writer.writerow(user.values())


def _get_report_maker(format):
    if format == 'csv':
        return _dict_to_csv
    elif format == 'tsv':
        return _dict_to_tsv
    elif format == 'json':
        return _dict_to_json
    else:
        return 0


class ReportMaker:
    def make_report(self, data, format, output_path):
        # определяет, какой метод будет вызываться в зависимости от формата
        report_maker = _get_report_maker(format)
        return report_maker(data, output_path)
