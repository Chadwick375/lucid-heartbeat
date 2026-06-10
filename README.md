# lucid-heartbeat

Free, **laptop-independent** uptime pinger that keeps the [Lucid Academy](https://lucidai.pro)
autonomous engine ticking **24/7**.

GitHub Actions hits the engine's key-protected tick endpoint every 5 minutes from
GitHub's cloud, so the content engine, social autopilot, support bot, and crons
keep running even if every local machine is off. A daily `keepalive` commit stops
GitHub from auto-disabling the schedule, so it runs **forever**.

No secrets live in this repo — the cron key is an encrypted GitHub Actions secret
(`LUCID_CRON_KEY`), masked in all logs. The tick endpoint does nothing without it.
