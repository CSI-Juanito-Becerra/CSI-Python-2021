import requests
import bs4

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.4663&lon=-66.1047#.YjoGyRDMK3I")
soup = bs4.BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[1]
print(tonight.prettify())


