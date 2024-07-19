import requests
import re
import time
import random
from colorama import Fore, init
banner()
# Initialize colorama
init(autoreset=True)

# Color definitions
COLORS = {
    "luc": Fore.GREEN,
    "trang": Fore.WHITE,
    "do": Fore.RED,
    "vang": Fore.YELLOW,
    "hong": Fore.MAGENTA,
    "xduong": Fore.BLUE,
    "xnhac": Fore.CYAN,
}

# Function to check Facebook login using a cookie
def check_login_facebook(cookie):
    try:
        response = requests.get("https://m.facebook.com/profile.php", cookies={"cookie": cookie}).text
        fb_dtsg = re.search(r'name="fb_dtsg" value="([^"]+)"', response).group(1)
        jazoest = re.search(r'name="jazoest" value="([^"]+)"', response).group(1)
        idacc = re.search(r'name="target" value="([^"]+)"', response).group(1)
        name = re.search(r'<title>([^<]+)</title>', response).group(1)
        return name, fb_dtsg, jazoest, idacc
    except Exception as e:
        print(f"Error during login check: {e}")
        return False

# Display a visual delay
def visual_delay(t):
    start_time = time.time()
    while time.time() - start_time < t:
        remaining_time = int(t - (time.time() - start_time))
        for step in ["LOADING ", "LOADING.", "LOADING..", "LOADING..."]:
            print(f"\r{COLORS['do']}[\033[1;33mvLongzZ{COLORS['do']}] {COLORS['luc']} ~> {step} {COLORS['do']} | {remaining_time} | \r", end='')
            time.sleep(0.14)
    print("\r\033[1;95m \033[1;97m                         \r", end='')

# Main function
def main():
    cookie = input(" \033[1;97m[\033[1;31mvL\033[1;97m] => \033[38;5;222mNhập Cookie: ")
    login_info = check_login_facebook(cookie)

    if login_info:
        name, fb_dtsg, jazoest, idacc = login_info
        print(f" \033[1;97m[\033[1;31mvL\033[1;97m] => \033[38;5;223mLogin Thành Công")
        time.sleep(2)
        print(f" \033[1;97m[\033[1;31mvL\033[1;97m] => \033[38;5;224mTên Tài Khoản: {COLORS['hong']}{name}")
        print(f" \033[1;97m[\033[1;31mvL\033[1;97m] => \033[38;5;225mID Tài Khoản: {COLORS['hong']}{idacc}")
        print("\033[1;97m─────────────────────────────────────────────────────────")
    else:
        print(f" \033[1;97m[\033[1;31mvL\033[1;97m] => \033[38;5;226mLogin Thất Bại")
        return

    comments = []
    print("Nhập các bình luận. Nhấn Enter để dừng:")
    while True:
        comment = input("Nhập bình luận: ")
        if comment.strip() == "":
            break
        comments.append(comment)

    if not comments:
        print("Không có bình luận nào được nhập. Thoát.")
        return

    try:
        dem = int(input(f"{COLORS['vang']}\033[38;5;111mNhập Số Lần CMT ( Nhập Nhiều Lên Để Đỡ Bị Lỗi ):\033[1;33m "))
        delay_min = float(input(f"{COLORS['vang']}\033[38;5;112mNhập Thời Gian Chờ Tối Thiểu (Giây):\033[1;33m "))
        delay_max = float(input(f"{COLORS['vang']}\033[38;5;113mNhập Thời Gian Chờ Tối Đa (Giây):\033[1;33m "))
        print('Vào Web Rồi Lấy Link Bài Biết Bên Thanh Tìm Kiếm')
        link_m = input(f"{COLORS['vang']}\033[1;92mNhập Link Dưới Dạng m.facebook.com:\033[1;33m ")
    except ValueError as ve:
        print(f"Lỗi: {ve}. Vui lòng nhập đúng định dạng số.")
        return

    print(f"{COLORS['do']}══════════════════════{COLORS['luc']}Running{COLORS['do']}-Tools{COLORS['do']}══════════════════════")

    comment_index = 0  # Starting index
    total_comments = len(comments)

    for i in range(dem):
        if comment_index >= total_comments:
            comment_index = 0  # Reset to the first comment if out of comments

        try:
            get_cmt = requests.get(link_m, cookies={"cookie": cookie}).text
            action_url = re.search(r'form method="post" action="([^"]+)"', get_cmt).group(1)
            action_url = action_url.replace('&amp;', '&')
            fb_dtsg = re.search(r'name="fb_dtsg" value="([^"]+)"', get_cmt).group(1)
            jazoest = re.search(r'name="jazoest" value="([^"]+)"', get_cmt).group(1)
            comment_text = comments[comment_index]  # Use the current index to get comment
            comment_index += 1  # Move to the next comment
            icon = '🎊🎉💕💛❤💘💚💖💙💓💝💟💔💜💞💜💞💗💗'
            result_ico = ''.join(random.choice(icon) for _ in range(2))
            noidung = f'{comment_text}{result_ico}'
            post_data = {
                'fb_dtsg': fb_dtsg,
                'jazoest': jazoest,
                'comment_text': noidung
            }
            comment_response = requests.post(f'https://m.facebook.com{action_url}', data=post_data, cookies={"cookie": cookie})
            if comment_response.status_code == 200:
                print(f" \033[1;97m[\033[1;31mvL\033[1;97m] => {COLORS['luc']}Comment \033[1;33m{i+1}/{dem} \033[1;92mthành công!")
            else:
                print(f" \033[1;97m[\033[1;31mvL\033[1;97m] => {COLORS['do']}Comment \033[1;33m{i+1}/{dem} \033[1;31mthất bại!")
            delay = random.uniform(delay_min, delay_max)
            visual_delay(delay)
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
