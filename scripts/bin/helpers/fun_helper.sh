FUN=$(dirname ${BASH_SOURCE[0]})

function print_done() {
  cat "${FUN}/done.txt"
}
