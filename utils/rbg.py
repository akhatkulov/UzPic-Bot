import aiohttp
import asyncio
import logging

from photo import photo_link
async def download_image(image_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            if response.status != 200:
                logging.error(f"Error downloading image: {response.status}")
                return None
            image_data = await response.read()
            return image_data
        
x = download_image(img_url="http://telegra.ph//file/9136c885619ea25f2e309.jpg")    
print(x)