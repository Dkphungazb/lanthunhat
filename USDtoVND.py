import requests

from bs4 import BeautifulSoup

def get_exchange_rate():
    # Lấy thông tin từ trang web của Vietcombank
    url = "https://www.vietcombank.com.vn/exchangerates/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Tìm tỷ giá USD/VND
    table = soup.find("table", id="ctl00_Content_ExrateView")
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            currency = cells[0].text.strip()
            if currency == "USD":
                buy_rate = float(cells[2].text.strip().replace(",", ""))
                sell_rate = float(cells[3].text.strip().replace(",", ""))
                return (buy_rate + sell_rate) / 2

def convert_usd_to_vnd(amount):
    rate = get_exchange_rate()
    return amount * rate

# Quy đổi 100 USD sang VND
result = convert_usd_to_vnd(100)
print(f"100 USD = {result:.0f} VND")
