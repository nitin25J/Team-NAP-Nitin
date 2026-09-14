import requests

BASE_URL = "http://localhost:8000/api"

endpoints = [
    "/hospitals/",
    "/rescue/",
    "/reports/",
    "/reports/verified",
    "/resources/",
    "/prediction/",
    "/prediction/all",
    "/dashboard/",
    "/dashboard/overview",
    "/dashboard/top-districts",
    "/dashboard/quick-links",
    "/dashboard/recent-activity",
    "/alerts/",
    "/alerts/active"
]

success = True
for ep in endpoints:
    url = f"{BASE_URL}{ep}"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            print(f"PASS: {ep}")
        else:
            print(f"FAIL: {ep} - Status {resp.status_code}")
            success = False
    except Exception as e:
        print(f"ERROR: {ep} - {e}")
        success = False

if not success:
    exit(1)
print("\nAll Backend Endpoints Passed!")
