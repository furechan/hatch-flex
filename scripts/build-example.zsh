#! /bin/zsh

set -eu 

rootdir=${0:a:h:h}

python -mbuild -n $rootdir/example

