from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Ouvrir le navigateur
driver = webdriver.Chrome()

# Aller sur GitHub
url = "https://github.com/search?q=mental+health+ai&type=repositories"
driver.get(url)

# Attendre que la page charge
time.sleep(3)

repos = []

# Trouver les repos
items = driver.find_elements(By.CSS_SELECTOR, "[data-testid='results-list'] > div")

for item in items:
    try:
        titre = item.find_element(By.CSS_SELECTOR, "a[href]").text.strip()
        url_repo = item.find_element(By.CSS_SELECTOR, "a[href]").get_attribute("href")
        
        try:
            description = item.find_element(By.TAG_NAME, "p").text.strip()
        except:
            description = "N/A"

        repos.append({
            "titre": titre,
            "url": url_repo,
            "description": description
        })
    except:
        pass

# Afficher et sauvegarder
df = pd.DataFrame(repos)
print(df)
df.to_csv("github_repos.csv", index=False)
print("✅ Sauvegardé : github_repos.csv")

driver.quit()