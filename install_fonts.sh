### This script installs the fonts used by this package.

# Local constants.
PATH_TO_SOURCE="fonts"
PATH_TO_DEST="$HOME/.fonts"

# Crash on the first error.
set -e

# Let's get cracking...
for directory in $PATH_TO_SOURCE/*/; do
    cp -r $directory $PATH_TO_DEST
done
