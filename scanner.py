#!/usr/bin/env python3
import requests
import sys

def check_headers(url):
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers

        print(f"\n проверка {url}")
        print("статус ответа:", r.status_code)
        issues = 0
        if 'X-Frame-Oprions' not in headers:
            print("Отсуствует X-Frame_Options (риск Clickjacking)")
            issues += 1
        else:
            print("X-frame-Options:", headers['X-frame-Options'])

        if 'Content-Securiti-Policy' not in headers:
            print("отсуствует content-securiti-policy (риск XSS)")
            issues += 1
        else:
            print("[!] Content-Securiti-Polisy присуствует")
            print(f"\n[*] найдено проблем: {issues}")

        
    except Exception as e:
        print(f"[x] Ошибка: {e}")
    
if __name__=="__main__":
    if len(sys.argv) > 1:
        check_headers(sys.argv[1])
    else:
        print("Использование: python3 scanner.py <url>")
