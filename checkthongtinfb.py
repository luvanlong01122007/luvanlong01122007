import requests
import urllib3

# Vô hiệu hóa cảnh báo không an toàn
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_facebook_info(facebook_id):
    url = f"https://dichvukey.site/api/fb.php?id={facebook_id}"

    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Kiểm tra xem yêu cầu có thành công không
        data = response.json()

        # Kiểm tra xem API có trả về đúng dữ liệu không
        if not data:
            return "No data received from the API."

        # Lấy dữ liệu từ phản hồi API
        name = data.get("name", "N/A")
        username = data.get("username", "N/A")
        about = data.get("about", "N/A")
        link = data.get("link", "N/A")
        total_count = data.get("total_count", "N/A")
        birthday = data.get("birthday", "N/A")
        gender = data.get("gender", "N/A")
        relationship_status = data.get("relationship_status", "N/A")

        # Tạo thông điệp để in ra
        message = (
            f"Tên: {name}\n"
            f"Username: {username}\n"
            f"Tổng Số Người Theo Dõi: {total_count}\n"
            f"About: {about}\n"
            f"Link FB: {link}\n"
            f"Sinh Nhật: {birthday}\n"
            f"Gender: {gender}\n"
            f"Relationship Status: {relationship_status}"
        )

        return message

    except requests.exceptions.RequestException as e:
        return f"Error fetching data from API: {str(e)}"

def get_post_id(linkpost):
    url = f'https://dichvukey.site/api/uid.php?uid={linkpost}'
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Kiểm tra xem yêu cầu có thành công không
        data = response.json()
        post_id = data.get('id', 'N/A')
        return post_id
    except requests.exceptions.RequestException as e:
        return f"Error fetching post ID from API: {str(e)}"

if __name__ == "__main__":
    linkpost = input("Nhập Link Bài Viết: ")
    post_id = get_post_id(linkpost)
    vanlong(14)
    
    if post_id.startswith("Error"):
        print(post_id)
    else:
        message_to_print = get_facebook_info(post_id)
        print(message_to_print)