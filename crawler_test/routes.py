from crawlee.crawlers import PlaywrightCrawlingContext
from crawlee.router import Router
from playwright.async_api import Route

router = Router[PlaywrightCrawlingContext]()


@router.default_handler
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    """Default request handler."""
    context.log.info(f'Processing {context.request.url} ...')

    # Preparing data to be pushed to the dataset
    url = context.request.url
    status = context.response.status
    headers = dict(context.response.headers)
    response_body = await context.response.text()
    
    await context.push_data(
        {
            'url': url, 
            'status': status,   
            'headers': headers,
            'response_body': response_body,
        }
    )

    await context.enqueue_links(
        selector='a',
        strategy='same-domain',
    )

