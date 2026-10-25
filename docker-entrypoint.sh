#!/bin/sh
set -eu

# Opt in on exactly one release job, rather than racing every worker startup.
if [ "${RUN_MIGRATIONS:-0}" = "1" ]; then
    python manage.py migrate --noinput
fi

exec "$@"
