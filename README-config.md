Absolutely. Here is the plain-text README you can copy into `README.md`. I've kept it short and included the configuration we have actually established, with placeholders for the details we haven't confirmed yet.

# Dental Dynamix Server Configuration

Short reference for maintaining the Dental Dynamix Django production server.

## Server

* Hostname: `dentaldynamix-webserver`
* OS: Ubuntu Linux
* Server user: `dentaldynamix-admin`
* Project: `/home/dentaldynamix-admin/dental-dynamix`
* Virtual environment: `/home/dentaldynamix-admin/dental-dynamix/.venv`
* Server IP: `192.168.1.95`
* Domain: `dentaldynamix.co.uk`
* WWW: `www.dentaldynamix.co.uk`

**Security:** Do not store passwords, API keys, Cloudflare tokens or private keys in this file.

## Django / Gunicorn

Django runs through Gunicorn using systemd.

* Service: `dental-dynamix.service`
* WSGI: `core.wsgi:application`
* Bind: `127.0.0.1:8000`
* Workers: `3`

Useful commands:

```bash
sudo systemctl status dental-dynamix
sudo systemctl restart dental-dynamix
sudo journalctl -u dental-dynamix -n 100 --no-pager
```

## Nginx

Nginx acts as the local reverse proxy.

* Config: `/etc/nginx/sites-available/dental-dynamix`
* Enabled config: `/etc/nginx/sites-enabled/dental-dynamix`
* Listen: `80`
* Proxy: `http://127.0.0.1:8000`

Configured domains:

```text
dentaldynamix.co.uk
www.dentaldynamix.co.uk
```

Useful commands:

```bash
sudo nginx -t
sudo systemctl reload nginx
sudo systemctl status nginx
```

## Cloudflare Tunnel

Cloudflare Tunnel provides the public connection to the server.

* Service: `cloudflared.service`
* Executable: `/usr/bin/cloudflared`
* Token file: `/etc/cloudflared/token`
* Origin: `http://localhost:80`

Configured hostnames:

```text
dentaldynamix.co.uk       → http://localhost:80
www.dentaldynamix.co.uk   → http://localhost:80
```

Useful commands:

```bash
sudo systemctl status cloudflared
sudo journalctl -u cloudflared -n 50 --no-pager
```

The tunnel connects outbound to Cloudflare, so the web server does not need to be directly exposed to the internet.

## Database

* Engine: `REPLACE_WITH_DATABASE_ENGINE`
* Database name: `REPLACE_WITH_DATABASE_NAME`
* Database user: `REPLACE_WITH_DATABASE_USER`
* Database host: `REPLACE_WITH_DATABASE_HOST`
* Database port: `REPLACE_WITH_DATABASE_PORT`

**Do not put the database password in this README.**

## Services

All three production services are enabled at boot:

```text
dental-dynamix.service   enabled
nginx.service            enabled
cloudflared.service      enabled
```

Check:

```bash
sudo systemctl is-enabled dental-dynamix
sudo systemctl is-enabled nginx
sudo systemctl is-enabled cloudflared
```

## Request Flow

```text
Visitor
   ↓
Cloudflare
   ↓
Cloudflare Tunnel
   ↓
Nginx :80
   ↓
Gunicorn 127.0.0.1:8000
   ↓
Django
   ↓
Database
```

## Current Setup Note

The current Django `500 Internal Server Error` is expected because the SEO page/configuration records have not yet been created in the Django admin.

Therefore, the `500` response from:

```bash
curl -I http://127.0.0.1:8000
```

and:

```bash
curl -I -H "Host: dentaldynamix.co.uk" http://127.0.0.1
```

is currently expected and does **not** indicate that Gunicorn, Nginx or Cloudflare Tunnel is broken.

## Before Changing Nameservers

Do **not** change the domain nameservers until the following are confirmed:

```text
✓ Django/Gunicorn running
✓ Nginx running
✓ Cloudflared running
✓ Cloudflare Tunnel connected
✓ dentaldynamix.co.uk configured in the tunnel
✓ www.dentaldynamix.co.uk configured in the tunnel
✓ Nginx configured for both domains
✓ SEO/admin pages created
✓ Website tested successfully
```

Once these are all ready, the domain nameservers can be changed to Cloudflare.

## Deployment Checklist

```text
1. Update Django/application
2. Run migrations if required
3. Collect static files if required
4. Restart dental-dynamix
5. Check Gunicorn logs
6. Check Nginx configuration
7. Reload Nginx
8. Check Cloudflare Tunnel
9. Test website
10. Only then change nameservers to Cloudflare
```

## Dental Dynamix – Final TODO

* complete all pages and test them
* update contact form emailing service and test
* pick and change images to match stying
* test all buttons and links
* update SEO app to match new pages
* get partners logos ready for the site
* git DJ access to cloudflare admin portal for the website
* Once site is complete remove under construction in admin and update the nginx to allow other pages: sudo nano /etc/nginx/sites-enabled/dental-dynamix
