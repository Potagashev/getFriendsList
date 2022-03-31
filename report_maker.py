import csv
import json
import constants


def to_json(data, header=None, output_path=constants.OUTPUT_PATH):
    string = json.dumps(data, ensure_ascii=False, indent=4)
    my_file = open(output_path, "w", encoding="utf-8")
    my_file.write(string, )
    my_file.close()


def to_csv(data, headers, output_path=constants.OUTPUT_PATH):
    # pprint(data)
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def to_tsv(data, headers, output_path=constants.OUTPUT_PATH):
    with open(output_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(headers)

        for user in data:
            writer.writerow(user.values())


def get_report_maker(format):
    if format == 'CSV':
        return to_csv
    elif format == 'TSV':
        return to_tsv
    elif format == 'JSON':
        return to_json
    else:
        raise ValueError(format)


class ReportMaker:
    def make_report(self, data, headers, format, output_path):
        report_maker = get_report_maker(format)
        return report_maker(data, headers, output_path)