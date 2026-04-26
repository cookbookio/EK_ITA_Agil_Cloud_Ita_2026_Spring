#!/usr/bin/env python3
"""
HTTP Requester — send N requests to a remote IP at a fixed interval.

Usage:
    python http_requester.py <url> [options]

Examples:
    python http_requester.py http://192.168.1.100          # 10 requests, 1s apart
    python http_requester.py http://192.168.1.100:8080/api -n 50 -i 0.5
    python http_requester.py https://example.com -n 5 -i 2 -m POST -d '{"key":"value"}'
"""

import argparse
import time
import sys
import json
import urllib.request
import urllib.error


def send_request(url: str, method: str, headers: dict, data: bytes | None) -> tuple[int, str]:
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        return 0, str(e.reason)
    except Exception as e:
        return 0, str(e)


def main():
    parser = argparse.ArgumentParser(
        description="Send HTTP requests to a remote IP at a fixed interval."
    )
    parser.add_argument("url", help="Target URL, e.g. http://192.168.1.100:8080/api")
    parser.add_argument("-n", "--count", type=int, default=10,
                        help="Number of requests to send (default: 10)")
    parser.add_argument("-i", "--interval", type=float, default=1.0,
                        help="Seconds between requests (default: 1.0)")
    parser.add_argument("-m", "--method", default="GET",
                        help="HTTP method (default: GET)")
    parser.add_argument("-d", "--data", default=None,
                        help="Request body (string or JSON)")
    parser.add_argument("-H", "--header", action="append", default=[],
                        metavar="KEY:VALUE", help="Extra headers (repeatable)")
    parser.add_argument("--no-summary", action="store_true",
                        help="Skip the summary at the end")
    args = parser.parse_args()

    # Build headers
    headers = {"User-Agent": "http-requester/1.0"}
    for h in args.header:
        if ":" not in h:
            print(f"[WARN] Skipping malformed header: {h!r} (expected KEY:VALUE)")
            continue
        key, _, value = h.partition(":")
        headers[key.strip()] = value.strip()

    # Build body
    body = None
    if args.data:
        body = args.data.encode("utf-8")
        if "Content-Type" not in headers:
            # Auto-detect JSON
            try:
                json.loads(args.data)
                headers["Content-Type"] = "application/json"
            except ValueError:
                headers["Content-Type"] = "text/plain"

    method = args.method.upper()
    results = []

    print(f"Target  : {args.url}")
    print(f"Method  : {method}")
    print(f"Requests: {args.count}  |  Interval: {args.interval}s")
    print("-" * 55)

    for i in range(1, args.count + 1):
        start = time.time()
        status, body_resp = send_request(args.url, method, headers, body)
        elapsed = time.time() - start

        ok = "✓" if 200 <= status < 300 else "✗"
        preview = body_resp[:80].replace("\n", " ")
        print(f"[{i:>4}/{args.count}] {ok} {status}  {elapsed:.3f}s  {preview}")

        results.append({"status": status, "elapsed": elapsed})

        if i < args.count:
            time.sleep(args.interval)

    if not args.no_summary:
        print("-" * 55)
        total = len(results)
        success = sum(1 for r in results if 200 <= r["status"] < 300)
        avg_ms = (sum(r["elapsed"] for r in results) / total) * 1000
        print(f"Done — {success}/{total} successful  |  avg response: {avg_ms:.1f}ms")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(0)
