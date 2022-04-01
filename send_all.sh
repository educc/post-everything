#!/bin/sh


showHelp() {
  echo "Params required."
  echo "Usage: ./send_all.sh https://myhost.com/path/subpath"
}

[ "$#" -eq 1 ] || { showHelp; exit 1; }

for filename in *.csv;
do
  url="$1/$filename"
  curl -F file=@$filename "$url"
done