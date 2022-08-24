FROM caddy:2.5.2-builder-alpine AS builder

RUN xcaddy build \
        --with github.com/caddy-dns/ionos

FROM caddy:2.5.2
COPY --from=builder /usr/bin/caddy /usr/bin/caddy
COPY ./Caddyfile /etc/caddy/Caddyfile
