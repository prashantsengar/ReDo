import random
import requests

text_url = 'http://localhost:5000/text/'
video_url = 'http://localhost:5000/video/'


def get_object():
    obj = ['bottle', 'matchbox', 'wool', 'button', 'socks','ice cream sticks', 'cd']
    return random.choice(obj)

def get_text_data(obj):
    
    text = requests.get(text_url+obj)
    text = text.json()


    for i in range(len(text)):
        a = text[str(i)]
        url, title = a[0], a[1]
        print(f'Tutorial: {title}')
        print(f'URL: {url}')
        print('\t\t---')

def get_video_data(obj):
    videos = requests.get(video_url+ obj).json()
    for i in range(len(videos)):
        a = videos[str(i)]
        url, title, desc = a[0], a[1], a[2]
        print(f'Video: {title}')
        print(f'-> {desc}')
        print(f'URL: {url}')
        print('\t\t---')


def main():
    print('Click picture\n\n')
    obj = get_object()

    get_text_data(obj)
    get_video_data(obj)

    
if __name__=='__main__':
    main()
