#!/usr/bin/bash
function create_virtenv () {
pyenv install $1
pyenv global "$1"
pyenv virtualenv python$1
pyenv global 3.7.1
}
create_virtenv 3.7.2
create_virtenv 2.7.6
