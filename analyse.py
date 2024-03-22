import socket
import geoip2.database
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse


def browser(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get("https://" + url)
    driver.set_window_size(1920, 1080)  

    driver.save_screenshot("homepage.png")


    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(1920, required_height) 
    driver.save_screenshot("full_homepage.png")
    driver.quit()

def ip(url):
    server_ip = socket.gethostbyname(url)
    print("Server IP:", server_ip)
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    response = reader.city(server_ip)
    print("Server Location:", response.city.name, response.country.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assess the risk of URLs by analyzing server insights and capturing home page snapshots")
    parser._action_groups.pop()
    required = parser.add_argument_group('Required arguments')
    required.add_argument('--url', help="URL to check", required=True)
    args = parser.parse_args()
    browser(args.url)
    ip(args.url)
