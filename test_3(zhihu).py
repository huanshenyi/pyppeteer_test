import asyncio
import time, random
from pyppeteer import launch
from exe_js import js1, js5, js3, js4


def input_time_random():
    return random.randint(100, 151)


async def get_cookie(page):
    res = await page.content()
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1};'
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print('cookies:', cookies)
    return cookies


async def login(username, pd, url):
    browser = await launch({'headless': False, 'args': ['--no-sandbox'], })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto(url)
    await page.evaluate(js1) #在网页中执行js代码
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    await page.type('.SignFlow-account .Input', username, {'delay': input_time_random() - 50})
    await page.type('.SignFlow-password .Input', pd, {'daelay': input_time_random()})
    time.sleep(2)
    await page.click('.Button.SignFlow-submitButton.Button--primary.Button--blue')
    page.mouse # 鼠标模拟点击
    await page.waitFor(20)
    await page.waitForNavigation()
    print(page.url)
    await get_cookie(page)


if __name__ == '__main__':
    username = 'sukangshou4@163.com'
    pd = 'niangu98'
    url = 'https://www.zhihu.com/signin?next=%2Fhot'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(login(username, pd, url))
