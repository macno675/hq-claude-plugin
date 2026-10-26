#!/usr/bin/env python3
"""LCSC Agent API (podpisane żądania). Użycie:
  lcsc.py search "<słowa>" [--in-stock] [--limit N] [--currency USD]
  lcsc.py detail C25804 [--currency USD]
Klucze: zmienne LCSC_APP_KEY, LCSC_SECRET. Wynik: TSV (tanie w tokenach).
"""
import hashlib, json, os, secrets, string, sys, time
import urllib.error, urllib.parse, urllib.request

BASE = "https://api.lcsc.com/rest/api/agent/product/v1/"


def sign(key, secret, nonce, ts, params):
    biz = {k: (json.dumps(v, separators=(",", ":")) if isinstance(v, (dict, list)) else str(v))
           for k, v in params.items() if v is not None}
    biz = urllib.parse.urlencode(sorted(biz.items()))
    base = f"key={key}&nonce={nonce}&secret={secret}&timestamp={ts}"
    return hashlib.sha256((base + "&" + biz if biz else base).encode()).hexdigest()


def call(path, params):
    key, secret = os.environ.get("LCSC_APP_KEY"), os.environ.get("LCSC_SECRET")
    if not (key and secret):
        sys.exit("Brak LCSC_APP_KEY / LCSC_SECRET (wniosek: https://www.lcsc.com/agent/apply)")
    nonce = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
    ts = str(int(time.time()))
    headers = {"key": key, "nonce": nonce, "timestamp": ts, "signature": sign(key, secret, nonce, ts, params)}
    url = BASE + path + "?" + urllib.parse.urlencode(params)
    try:
        r = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read()[:300].decode(errors='replace')}")
    if not r.get("success"):
        sys.exit(f"API {r.get('code')}: {r.get('message')}")  # 429/430 limity, 4003 uwierzytelnianie, 5002 IP
    return r["result"]


def row(p):
    pr = p.get("productPrice") or {}
    tiers = pr.get("standardPricing") or []
    price = " ".join(f"{t['breakQuantity']}+:{t['unitPrice']}" for t in tiers[:4])
    params = ";".join(f"{k}={v}" for k, v in (p.get("productParameters") or {}).items())
    mfr = (p.get("manufacturer") or {}).get("name", "")
    return "\t".join(str(x) for x in (
        p.get("lcscProductNumber"), p.get("manufacturerProductNumber"), mfr, p.get("package"),
        pr.get("quantityAvailable", ""), price, p.get("minimumOrderQuantity"),
        p.get("datasheetURL"), params))


HEAD = "lcsc\tmpn\tmfr\tpackage\tstock\tprice_breaks\tmoq\tdatasheet\tparams"


def main(a):
    if len(a) < 2 or a[0] not in ("search", "detail"):
        sys.exit(__doc__)
    opt = lambda n, d: a[a.index(n) + 1] if n in a else d
    cur = opt("--currency", "USD")
    if a[0] == "search":
        res = call("keywordsearch", {"keyword": a[1], "returnInformation": "All", "currency": cur,
                                      "inStockOnly": "true" if "--in-stock" in a else "false",
                                      "offset": "1", "limit": opt("--limit", "20")})
        print(HEAD)
        for p in res.get("products", []):
            print(row(p))
        print(f"# total={res.get('productCount')} nextOffset={res.get('nextOffset')}")
    else:
        res = call("productdetails", {"lcscProductNumber": a[1], "currency": cur, "returnInformation": "All"})
        print(HEAD)
        print(row(res))


if __name__ == "__main__":
    main(sys.argv[1:])
