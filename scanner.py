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
        if 'X-Frame-Options' not in headers:
            print("Отсутствует X-Frame-Options (риск Clickjacking)")
            issues += 1
        else:
            print("X-Frame-Options:", headers['X-Frame-Options'])

        if 'Content-Security-Policy' not in headers:
            print("отсуствует content-securiti-policy (риск XSS)")
            issues += 1
        else:
            print(" Content-Security-Polisy присутствует")
            print(f"\n найдено проблем: {issues}")

        
    except Exception as e:
        print(f"[x] Ошибка: {e}")
    
if __name__=="__main__":
    if len(sys.argv) > 1:
        check_headers(sys.argv[1])
    else:
        print("Использование: python3 scanner.py <url>")
