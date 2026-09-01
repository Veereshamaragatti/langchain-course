import truststore

truststore.inject_into_ssl()

import requests

response = requests.get(
    "https://api.smith.langchain.com/info",
    timeout=20,
)

print("Status:", response.status_code)
print("SSL connection succeeded")