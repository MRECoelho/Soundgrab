import subprocess

DEFAULT_CONFIG = 'ytdl -x --audio-format "mp3" --audio-quality 9 --restrict-filenames'

url_list = []
    
while True:
    url_input = input("enter url: ")
    if url_input:
        url_list.append(url_input)
    else:
        break

def create_cmd(default_config, url):
    return f'{default_config} {url}'

print(f"{len(url_list)} url(s) given.")
for url in url_list:
    print(f"Downloading content at {url}")
    cmd = create_cmd(DEFAULT_CONFIG, url)
    sp = subprocess
    sp.run(cmd)
print('Finished')