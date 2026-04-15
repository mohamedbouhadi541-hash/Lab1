import requests

url = "https://github.com/search?q=mental+health+ai&type=repositories"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")

with open("github_results.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("✅ Fichier sauvegardé : github_results.txt")