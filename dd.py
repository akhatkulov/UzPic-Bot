import requests

def remove_background(img_url):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': img_url,
            'size': 'auto'
        },
        headers={'X-Api-Key': 'YOUR_API_KEY_HERE'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
        
        with open('no-bg.png','rb') as f:
            x = f.read()
            return x
    else:
        return "Error in API"

# Replace 'YOUR_API_KEY_HERE' with your actual API key
img_url = "http://telegra.ph//file/8bbaaa83432ac82cc5875.jpg"
result = remove_background(img_url)
print(result)
