XCLIP='xclip'

function copy_value() {
  if [ "$(uname)" == "Darwin" ]; then
      echo "$1" | pbcopy
  else
      echo "$1" | "$XCLIP" -selection c
  fi
}

function open_value() {
  if [ -n "$1" ]; then
    if [ "$(uname)" == "Darwin" ]; then
      open "$1"
    else
         nohup xdg-open "$1" >/dev/null 2>&1 &
    fi
  fi
}
