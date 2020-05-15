#!/bin/sh

SERVER=https://acme-dns.sembritzki.org/update
USER=f86ac634-a4fd-4b95-8a4e-fe24604d93c6
PASS=_pXHznqRg1NFTKNhy31_haKp8w0BMIkcYUUAy_pl
DOMAIN=01ba4bae-5832-4c62-a0dc-30973dcba9b6
TOKEN=$4

echo "HOOK: $@"

case "$1" in
    "deploy_challenge")
        curl -X POST \
          -H "X-Api-User: $USER" \
          -H "X-Api-Key: $PASS" \
          -d "{\"subdomain\": \"$DOMAIN\", \"txt\": \"$TOKEN\"}" \
          $SERVER
        ;;
    "clean_challenge")
        ;;
    "deploy_cert")
        # optional:
        # /path/to/deploy_cert.sh "$@"
        ;;
    "unchanged_cert")
        ;;
    "startup_hook")
        ;;
    "exit_hook")
        ;;
esac
