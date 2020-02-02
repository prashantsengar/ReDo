import requests

API_KEY = 'AIzaSyCF3NNU2ldXik4ZBD4fzckDfJjzD2jhkWs'

def get_search_results(q):
    page_token=''
    video_url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={q}&key={API_KEY}&pageToken={page_token}'
    videos = requests.get(video_url)
    print(video_url)
    video_data = videos.json()
    return video_data

def get_video_urls(video_data):
    items = video_data['items']
    videos = {}

    for i in range(3):
        vid = 'https://www.youtube.com/watch?v=' + items[i]['id']['videoId']
        title = items[i]['snippet']['title']
        desc = items[i]['snippet']['description']

        videos[i] = [vid, title, desc]
##        videos.append({i:[vid, title, desc]})

    return videos

def get_data(q):
    data = get_search_results(q)
    return get_video_urls(data)
