import requests

def download_file(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f'Vui Lòng Vào Lại TooL')
            print('cd /sdcard/download && python gopvip.py')
        else:
            print(f'Lỗi khi tải mã: {response.status_code}')
    except Exception as e:
        print(f'Lỗi: {str(e)}')

def main():
    url = 'https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/gopvip.py'
    filename = 'gopvip.py'
    download_file(url, filename)

if __name__ == '__main__':
    main()
