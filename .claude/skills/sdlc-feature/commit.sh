#!/bin/sh
# Local commit helper: fixed identity, subject line only (no body or trailers). Never pushes.
set -e
subject=$(printf '%s' "$1" | head -n 1)
git add -A -- . ':!.claude'
git -c user.name=developer -c user.email=developer@example.com commit -q -m "$subject"
git log --oneline -1
