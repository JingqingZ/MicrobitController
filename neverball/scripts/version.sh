#!/bin/sh

BUILD="$1"
VERSION="$2"
TEMPLATE_FILE="$3"
HEADER_FILE="$4"
CACHE_FILE="$5"

LC_ALL=C
export LC_ALL

svn_version()
{
    svn_rev="$(svnversion . /svn/neverball/trunk | tr : +)"
    case "$svn_rev" in
        [1-9]*) echo "r$svn_rev" ;;
        *) false ;;
    esac
}

git_version()
{
    if git_desc="$(git describe --dirty=+)"; then
        echo "$git_desc" | sed -e 's/^neverball-//' -e 's/-g/-/g'
    fi
}

if [ "$BUILD" != "release" ]; then
    VERSION="$(git_version || date -u +"%Y-%m-%d" || echo "$VERSION-dev")"
fi

if [ "$VERSION" != "$(cat "$CACHE_FILE" 2> /dev/null)" ]; then
    sed 's,0\.0\.0,'"$VERSION"',' < "$TEMPLATE_FILE" > "$HEADER_FILE"
    echo "$VERSION" > "$CACHE_FILE" 2> /dev/null
fi

echo "$VERSION"
