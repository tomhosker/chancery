### This script installs the fonts used by this package.

# Local constants.
PATH_TO_SOURCE="$(dirname "$0")/fonts"
PATH_TO_DEST="$HOME/.fonts"

# Crash on the first error.
set -e

#################
# INSTALL FONTS #
#################

# Check fonts folder exists.
if [ ! -d $PATH_TO_DEST ]; then
    mkdir -p $PATH_TO_DEST
fi

# Copy font folders across.
for directory in $PATH_TO_SOURCE/*/; do
    cp -ru $directory $PATH_TO_DEST
done
