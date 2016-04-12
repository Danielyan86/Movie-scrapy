import requests

url = "http://www.topit.me"
# headers = {
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
#     "Upgrade-Insecure-Requests": "1",
#     'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
cookie = {"is_click": "1"}
# bdshare_firstime=1460205650524; PHPSESSID=8ha45t9u1gt4fmoih3j01ha3n5; item-tip=true; tip_global_1=true; Hm_lvt_5256b9d21d9d68644fca1a0db29ba277=1460205595,1460208878,1460209384,1460288782; Hm_lpvt_5256b9d21d9d68644fca1a0db29ba277=1460294613; __utma=137188917.786675411.1460205597.1460288786.1460293793.5; __utmb=137188917.5.10.1460293793; __utmc=137188917; __utmz=137188917.1460288786.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
r = requests.Session().get(url, cookies=cookie)
if r.status_code == 200:
    print r.text

from selenium import webdriver

driver = webdriver.PhantomJS()
r = driver.get(url=url)
driver.save_screenshot('screen.png')
pass
