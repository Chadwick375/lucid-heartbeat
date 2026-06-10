#!/usr/bin/env python3
"""Send the watchdog alert email via SMTP. All inputs via env. Best-effort:
if SMTP secrets are missing or the send fails, it exits 0 (the workflow's own
failure already triggers GitHub's owner notification)."""
import os, sys, smtplib, ssl
from email.mime.text import MIMEText
host = os.environ.get("SMTP_HOST"); user = os.environ.get("SMTP_USER")
pwd = os.environ.get("SMTP_PASS"); to = os.environ.get("ALERT_TO")
port = int(os.environ.get("SMTP_PORT") or 465)
subj = os.environ.get("SUBJ", "Lucid watchdog"); body = os.environ.get("BODY", "")
if not (host and user and pwd and to):
    print("SMTP secrets incomplete; skipping email (GitHub failure notice still fires)"); sys.exit(0)
try:
    m = MIMEText(body, "html", "utf-8"); m["Subject"] = subj; m["From"] = user; m["To"] = to
    s = smtplib.SMTP_SSL(host, port, context=ssl.create_default_context(), timeout=30) if port == 465 else smtplib.SMTP(host, port, timeout=30)
    if port != 465: s.starttls(context=ssl.create_default_context())
    s.login(user, pwd); s.sendmail(user, [to], m.as_string()); s.quit()
    print("email sent to", to)
except Exception as e:
    print("email failed:", str(e)[:160])
