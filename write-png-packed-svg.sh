echo $#
if test $# -ne 1; then
  echo Usage: $0 somefile.svg
  exit 0
fi
inkscape $1 -C -o output.png
inkscape $1 --export-text-to-path --export-filename=output.svg
ls output.png output.svg
