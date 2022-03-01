PROJECTS=$(ls -d ~/otto/*  )
STANI=$(ls -d ~/stani/*  )

function list_projects() {
  cat << EOF
$PROJECTS
$STANI
EOF
}

function verify_fzf_installation() {
  if ! command -v fzf >/dev/null 2>&1; then
    echo "Needs the fzf package to run. You can install via brew/apt-get, or via the dev-setup playbook"
    exit 1;
  fi
}

function fzf_select_project() {
    list_projects | fzf --header 'select a project'
}

function fzf_single_select() {
  VALUE=$(echo "$1" | fzf)
  if [[ -z "$VALUE" ]]; then
    echo "Invalid option selected"
    exit 1;
  fi
  echo "$VALUE"
}

function fzf_multi_select() {
  VALUES=$(echo "$1" | fzf -m)
  if [[ -z "$VALUES" ]]; then
    echo "Invalid option selected"
    exit 1;
  fi
  echo "$VALUES"
}
