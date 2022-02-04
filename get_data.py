import os

url_to_path = {
    'https://www.youtube.com/watch?v=VKMw2it8dQY' : 'vid_data/yooh_vid.mp4',
    'https://www.youtube.com/watch?v=TWKr4R8k9Ew' : 'vid_data/prep_vid.mp4'
}

def download_video(url, location):
    os.system(f'youtube-dl {url} -o {location} -f mp4')

for url in url_to_path:
    download_video(url, url_to_path[url])

# download_video(yooh_url, 'vid_data/yooh_vid.mp4')
