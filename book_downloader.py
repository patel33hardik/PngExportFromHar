import os
import json
import base64

def download_preview(base64_data, save_path):
    image_data = base64.b64decode(base64_data)
    with open(save_path, 'wb') as f:
        f.write(image_data)

if __name__ == '__main__':
    file_path = '/Har_Data/page_452_to_528_ebookcentral.proquest.com.har'
    if not os.path.exists(file_path):
        print('File does not exist.')
        exit()

    with open(file_path, 'rb') as f:  # Open in binary mode
        data = f.read()
    har = json.loads(data.decode('utf-8'))


    output_folder = 'downloaded_images'
    os.makedirs(output_folder, exist_ok=True)

    i = 0
    for entry in har['log']['entries']:
        if 'docImage.action?encrypted=' in entry['request']['url']:
            if 'image/png' in entry['response']['content']['mimeType']:
                base64_data = entry['response']['content']['text']
                image_name = '{}_Image.png'.format(i)
                save_path = os.path.join(output_folder, image_name)
                download_preview(base64_data, save_path)
                print(f'Downloaded: {image_name}')
                i += 1

    print('Download completed.')