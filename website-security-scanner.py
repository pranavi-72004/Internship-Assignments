import requests

url = input("Enter Website URL: ")

try:
    response = requests.get(url, timeout=10)

    headers = response.headers

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    print("\nSecurity Scan Report")
    print("-" * 30)

    for header in security_headers:
        if header in headers:
            print(f"[✓] {header} Present")
        else:
            print(f"[✗] {header} Missing")

except Exception as e:
    print("Error:", e)
