echo $#
if test $# -ne 2; then
  echo Usage: $0 input.svg output-filename-without-extension
  exit 0
fi
inkscape $1 -C -o $2.png
inkscape $1 --export-text-to-path --export-filename=$2.svg
ls $2*
