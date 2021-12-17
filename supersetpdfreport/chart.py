from .config import PATH, SUPERSET_URL
from .logging import logger
import httpx
import sys
import asyncio
import time


async def compute_chart(client, access_token, chart_id):

    logger.debug("Compute and Cache Chart with ID: " + chart_id)
    Chart_URL="{}/api/v1/chart/{}/cache_screenshot/".format(SUPERSET_URL, chart_id)
    response = await client.get(
        Chart_URL,
        headers={"Authorization": "Bearer " + access_token},
    )
    if response.status_code == 200 or response.status_code == 202:
        data = response.json()
        cache_key = data["cache_key"]
        image_url = "{}/api/v1/chart/{}/screenshot/{}/".format(
            SUPERSET_URL, chart_id, cache_key
        )
        return image_url
    else:
        logger.error("{}: {}\nURL: {}".format(response.status_code, response.text, Chart_URL))
        sys.exit(1)


async def download_chart_screenshot(client, access_token, jobtype, chart_id, image_url):
    logger.debug("Download Chart with ID: " + chart_id)
    response = await client.get(
        image_url, headers={"Authorization": "Bearer " + access_token}
    )
    if response.status_code == 200:
        image = open("{}{}/images/chart_{}.png".format(PATH, jobtype, chart_id), "wb")
        image.write(response.content)
        image.close()
    else:
        logger.error("{}: {}".format(response.status_code, response.text))
        sys.exit(1)


async def get_chart_screenshots(access_token, jobtype, array_chart_id):

    async with httpx.AsyncClient() as client:
        task = []

        for chart_id in array_chart_id:
            task.append(
                asyncio.ensure_future(compute_chart(client, access_token, chart_id))
            )

        array_image_url = await asyncio.gather(*task)
        task.clear()

        # TODO: Needs to be improved
        time.sleep(10 + 5 * len(array_chart_id))

        for chart_id, image_url in zip(array_chart_id, array_image_url):
            task.append(
                asyncio.ensure_future(
                    download_chart_screenshot(
                        client, access_token, jobtype, chart_id, image_url
                    )
                )
            )

        return_code = await asyncio.gather(*task)
