from turtle import ht
from crawlee.crawlers import PlaywrightCrawler
from .routes import router

async def main() -> None:
    """The crawler entry point."""
    crawler = PlaywrightCrawler(
        request_handler=router,
        max_crawl_depth=1, # necessary to limit crawling only to the link(s) fetched from the main URL
    )

    await crawler.run(
        [
            'https://crawlee.dev',
        ]
    )
