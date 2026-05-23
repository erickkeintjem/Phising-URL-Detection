from db_helper import save_scan

save_scan(
    "http://secure-paypal-login.xyz",
    "PHISHING",
    94.7
)

save_scan(
    "https://google.com",
    "SAFE",
    98.2
)

print("Data inserted.")