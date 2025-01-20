from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

urls = [
    'https://groww.in/us-stocks/nke'
    # 'https://groww.in/us-stocks/ko',
    # 'https://groww.in/us-stocks/msft',
    # 'https://groww.in/stocks/m-india-ltd',
    # 'https://groww.in/us-stocks/axp',
    # 'https://groww.in/us-stocks/amgn',
    # 'https://groww.in/us-stocks/aapl',
    # 'https://groww.in/us-stocks/ba',
    # 'https://groww.in/us-stocks/csco',
    # 'https://groww.in/us-stocks/gs',
    # 'https://groww.in/us-stocks/ibm',
    # 'https://groww.in/us-stocks/intc',
    # 'https://groww.in/us-stocks/jpm',
    # 'https://groww.in/us-stocks/mcd',
    # 'https://groww.in/us-stocks/crm',
    # 'https://groww.in/us-stocks/vz',
    # 'https://groww.in/us-stocks/v',
    # 'https://groww.in/us-stocks/wmt',
    # 'https://groww.in/us-stocks/dis'
    ]

data = []
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and added to PATH
driver.maximize_window()

for url in urls:
    try:
        driver.get(url)
        time.sleep(5)  # Wait for initial page load

        company = driver.find_element(By.CSS_SELECTOR, "h1.usph14Head.displaySmall").text
        price = driver.find_element(By.CSS_SELECTOR, "uht141Pri contentPrimary displayBase").text

        # Use explicit wait for dynamic content
        try:
            change = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.uht141Day.bodyBaseHeavy.contentNegative"))
            ).text
        except Exception:
            change = "N/A"  # Default value if not found

        volume = driver.find_elements(By.CSS_SELECTOR, "table.tb10Table.col.l5 td")[1].text

        data.append([company, price, change, volume])

    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Save to Excel
df = pd.DataFrame(data, columns=["Company", "Price", "Change", "Volume"])
df.to_excel(r'C:\Users\Admin\Downloads\stocks1.xlsx', index=False)
print("Data saved to stocks.xlsx")
