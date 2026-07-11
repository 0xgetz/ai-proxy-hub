# Security Policy

## Supported deployment model

AI Gateway is designed primarily as a **local** proxy (loopback bind). Network
exposure requires explicit configuration and a strong server token.

## Hardening defaults

- Default `HOST` is `127.0.0.1` (local only).
- Binding beyond loopback (`0.0.0.0`, public interfaces) **requires** a non-empty
  `ANTHROPIC_AUTH_TOKEN` at startup.
- Admin UI (`/admin`) is loopback-only and rejects reverse-proxy forwarding headers.
- Telegram rejects all senders when `ALLOWED_TELEGRAM_USER_ID` is empty.
- Discord rejects all channels when `ALLOWED_DISCORD_CHANNELS` is empty.
- Managed env files written by admin / `aig-init` use mode `0600`.

## Reporting a vulnerability

Please open a private security advisory or contact the repository owner via
GitHub. Do not file public issues for unfixed remote code execution or auth
bypass reports.
