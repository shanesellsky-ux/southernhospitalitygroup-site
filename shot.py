import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for name,w,h in [('index',1440,900),('bourbon-street',1440,900),('red-river-gorge',1440,900),('index',390,844)]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.route('**/fonts.g*/**',lambda r:r.abort())
            await pg.goto(f'file:///home/claude/site/out/{name}.html'); await pg.wait_for_timeout(600)
            await pg.evaluate("document.querySelectorAll('img[loading]').forEach(i=>i.loading='eager')"); await pg.wait_for_timeout(800)
            await pg.screenshot(path=f'/tmp/s_{name}_{w}.png',full_page=True)
        await b.close()
asyncio.run(main())
