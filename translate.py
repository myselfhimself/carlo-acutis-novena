import csv
import os
import os.path

days = {}
DEFAULT_LANG = "fr"
TARGET_DIRECTORY = "dist"
os.makedirs(TARGET_DIRECTORY, exist_ok=True)


def render_as_png_packed_svg(original_svg_path):
    output_png_path = original_svg_path.split(".")[0] + ".png"
    output_svg_path = original_svg_path.split(".")[0] + "_text_as_path.svg"
    os.popen("inkscape {input_filename} -C -o {output_png_path}".format(input_filename=original_svg_path,
                                                                        output_png_path=output_png_path))
    os.popen("inkscape {input_filename} --export-text-to-path --export-filename={output_svg_path}".format(
        input_filename=original_svg_path, output_svg_path=output_svg_path))

with open("translations.csv") as csvfile:
    rows = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in rows:
        if row['day'] not in days:
            days[row['day']] = []
        days[row['day']].append({k: v for k, v in row.items() if k != 'day'})

for day_id, day in days.items():
    svg_filename_pattern = "day{day_id}_{lang}.svg"
    svg_filepath = os.path.join("day{day_id}".format(day_id=day_id),
                                svg_filename_pattern.format(day_id=day_id, lang=DEFAULT_LANG))

    for multilang_row in day:
        for lang in multilang_row:
            if lang != "fr":
                svg_translated_filepath = os.path.join(TARGET_DIRECTORY,
                                                       svg_filename_pattern.format(day_id=day_id, lang=lang))
                with open(svg_filepath, "r") as fin:
                    with open(svg_translated_filepath, "w") as fout:
                        for line in fin:
                            for day_str in day:
                                if day_str[DEFAULT_LANG] in line:
                                    line = line.replace(day_str[DEFAULT_LANG], day_str[lang])
                            fout.write(line)

                render_as_png_packed_svg(svg_translated_filepath)
