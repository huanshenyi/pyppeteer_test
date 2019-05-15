import pyppeteer
from pyppeteer import launch
import asyncio
from lxml import etree


async def main():

    browser = await launch()

    page = await browser.newPage()

    await page.goto("https://hlo.tohotheater.jp/net/movie/TNPI3090J01.do")

    doc = await page.content()
    #element Object
    titles = await page.xpath('//h2[@class="movies-title js-heightline-01"]')
    img_urls = await page.xpath("//div[@class='movies-image']/span")

    for title in titles:
        #text内容を取得
        title_str = await (await title.getProperty("textContent")).jsonValue()
        print(title_str)

    for url in img_urls:
        #tagの内容を取得
        url = await (await url.getProperty('style')).jsonValue()
        print(url)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

