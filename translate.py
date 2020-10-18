import csv
import glob
import shutil
import os
import os.path

days = {}
DEFAULT_LANG = "fr"
TARGET_DIRECTORY = "dist"
os.mkdir(TARGET_DIRECTORY)

with open("translations.csv") as csvfile:
    rows = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in rows:
        if row['day'] not in days:
            days[row['day']] = []
        days[row['day']].append({k:v for k,v in row.items() if k != 'day'})

for day_id, day in days.items():
    svg_filename_pattern = "j{day_id}_{lang}.svg"
    svg_filepath = os.path.join("day{day_id}".format(day_id), svg_filename_pattern.format(day_id=day_id, lang=DEFAULT_LANG))
    print(svg_filepath)
    print(day)
    print()

    for lang in day:
        if lang != "fr":
            svg_translated_filepath = os.path.join(TARGET_DIRECTORY, svg_filename_pattern.format(day_id=day_id, lang=lang))
            with open(svg_filepath, "r") as fin:
                with open(svg_translated_filepath, "w") as fout:
                    for line in fin:
                        for day_str in day:
                            fout.write(line.replace(day_str[DEFAULT_LANG], day_str[lang]))
