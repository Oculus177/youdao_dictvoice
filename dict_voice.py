import requests
import sys
import os
import time

def download_audio(audio, le):
    url = "https://dict.youdao.com/dictvoice"
    params = {
        "audio": audio,
        "le": le
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        timestamp = int(time.time())
        download_path = os.path.expanduser(f"~/Downloads/dict_voice_{timestamp}.mp3")
        with open(download_path, "wb") as f:
            f.write(response.content)
        print("音频文件下载成功！")
        print("文件保存在:", download_path)
    else:
        print("音频文件下载失败！")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dict_voice.py '<audio>' <le>")
        sys.exit(1)
    
    audio = sys.argv[1]
    le = sys.argv[2]
    download_audio(audio, le)
