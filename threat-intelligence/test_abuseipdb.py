import requests

API_KEY = "YOUR_ABUSEIPDB_API_KEY"

IP = "125.164.94.144"

response = requests.get(
    "https://api.abuseipdb.com/api/v2/check",
    headers={
        "Accept": "application/json",
        "Key": API_KEY
    },
    params={
        "ipAddress": IP,
        "maxAgeInDays": 90
    },
    timeout=15
)

data = response.json()["data"]

print("IP:", data["ipAddress"])
print("Country:", data["countryCode"])
print("ISP:", data["isp"])
print("Abuse Score:", data["abuseConfidenceScore"])
print("Reports:", data["totalReports"])
