from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


nickname = input("닉네임을 입력해주세요. : ")

def research():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)

    driver.get('https://op.gg')
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.TAG_NAME, "input")))

    driver.find_element_by_tag_name('input').click()
    driver.find_element_by_tag_name('input').send_keys(nickname)
    driver.find_element_by_class_name('summoner-search-form__button').click()

    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "SummonerRefreshButton")))
    driver.find_element_by_id('SummonerRefreshButton').click()

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
    except:
        pass

    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="right_gametype_soloranked"]/a')))
    driver.find_element_by_xpath('//*[@id="right_gametype_soloranked"]/a').click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "right_match"]')))

    html_code = driver.page_source

    return html_code

def get_info(html_code):
    html = BeautifulSoup(html_code, 'html.parser')

    name = html.select('.Name')[0].get_text()
    result = html.select('.GameResult')[0].get_text()
    game_length = html.select('.GameLength')[0].get_text()

    minute, second = game_length.split('분')
    second, second_a = second.split('초')

    result = ''.join(result.split())

    return name, minute, second, result

def in_game_playing():
    driver1 = webdriver.Chrome('chromedriver.exe')
    driver1.implicitly_wait(time_to_wait=3)
    driver1.get('https://www.op.gg/summoner/ajax/spectateStatus/summonerName={0}'.format(nickname))
    gaming_url_code = driver1.page_source

    gaming_html = BeautifulSoup(gaming_url_code, 'html.parser')
    print(gaming_html.find('pre').get_text())
    in_game_dict = eval(gaming_html.find('pre').get_text())

    if in_game_dict['className'] == 'Button SemiRound Green ':
        is_gaming = True
    else:
        is_gaming = False

    return is_gaming