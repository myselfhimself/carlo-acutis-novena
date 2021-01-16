#!/usr/bin/python
import csv
import os
import os.path
import shutil
import sys

days = {}
DEFAULT_LANG = "fr"
TARGET_DIRECTORY = "dist"
os.makedirs(TARGET_DIRECTORY, exist_ok=True)


def render_as_png_packed_svg(original_svg_path):
    output_png_path = original_svg_path.split(".")[0] + ".png"
    output_svg_path = original_svg_path.split(".")[0] + "_text_as_path.svg"
    os.popen("inkscape {input_filename} --export-background=\"#ffffff\" --export-background-opacity=255 -C -o {output_png_path}".format(input_filename=original_svg_path,
                                                                        output_png_path=output_png_path))
    os.popen("inkscape {input_filename} --export-text-to-path --export-filename={output_svg_path}".format(
        input_filename=original_svg_path, output_svg_path=output_svg_path))

if __name__ == "__main__":
    if sys.argv:
        TARGET_DIRECTORY = sys.argv[0]

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
    
        png_filename_pattern = "day{day_id}_{lang}.png"
        png_filepath = os.path.join("day{day_id}".format(day_id=day_id),
                                    png_filename_pattern.format(day_id=day_id, lang=DEFAULT_LANG))
    
        for multilang_row in day:
            for lang in multilang_row:
                lang_dir = os.path.join(TARGET_DIRECTORY, lang)
    
                os.makedirs(lang_dir, exist_ok=True)
    
                svg_translated_filepath = os.path.join(lang_dir,
                                                           svg_filename_pattern.format(day_id=day_id, lang=lang))
    
                png_translated_filepath = os.path.join(lang_dir,
                                                           png_filename_pattern.format(day_id=day_id, lang=lang))
                # If current iteration language is not the source language ie. french
                # translate SVG and re-render PNG and store into {TARGET_DIRECTORY}/{lang}/
                if lang != "fr":
                    with open(svg_filepath, "r") as fin:
                        with open(svg_translated_filepath, "w") as fout:
                            for line in fin:
                                for day_str in day:
                                    if day_str[DEFAULT_LANG] in line:
                                        line = line.replace(day_str[DEFAULT_LANG], day_str[lang])
                                fout.write(line)
    
                    render_as_png_packed_svg(svg_translated_filepath)
                else:
                    # If language is the source language (fr), just copy files as is into {TARGET_DIRECTORY}/{lang}/
                    shutil.copy2(svg_filepath, svg_translated_filepath)
                    shutil.copy2(png_filepath, png_translated_filepath)
