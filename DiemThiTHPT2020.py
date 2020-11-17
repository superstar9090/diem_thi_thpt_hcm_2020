#!/usr/bin/env python3
import subprocess
import unidecode
import json
from bs4 import BeautifulSoup
import csv

# import subprocess
# anloroi result = subprocess.check_output('curl -H "`oauth2l header --json key.json mobileinsights`" https://mobileinsights.googleapis.com/v2/networks', shell=True)

class Student:
	def __init__(self, name, birthday, point):
		self.name = name
		self.birthday = birthday
		self.point = point
	def toString(self):
		print("name : "+self.name + "\nbirthday : "+self.birthday + "\npoint : "+self.point)
# print('Hello World!')
list = []
row_list = [["Số báo danh","Tên", "Ngày sinh", "Tháng sinh", "Năm sinh", "Toán", "Ngữ Văn", "Lịch sử", "Vật lí", "Hóa học", "Địa lí", "Sinh học", "GDCD", "KHTN", "KHXH", "Tiếng anh"]]
subject_list = ["Toan", "Nguvan", "Lichsu", "Vatli", "Hoahoc", "Diali", "Sinhhoc", "GDCD", "KHTN", "KHXH", "TiengAnh"]
for x in range(100000):
	dataJson = {}
	c = x + 2000001
	curl = 'curl -F "SoBaoDanh='+"0"+str(c)+'" diemthi.hcm.edu.vn/Home/Show'
	print("curl : "+curl)
	result = subprocess.check_output([curl],shell=True, universal_newlines=True)
	# print(result)

	soup = BeautifulSoup(result, features="html.parser")
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out
	# print(soup.findAll("table"))
	gdp_table = soup.findAll("table")
	# print(len(gdp_table))
	if len(gdp_table) != 1:
		continue
	gdp_table_tr = gdp_table[0].find_all("tr")
	# print(gdp_table)

	gdp_table_td = gdp_table_tr[1].find_all('td')
	# print(gdp_table_td[0].getText())
	# print(gdp_table_td[1].getText())
	# print(gdp_table_td[2].getText())
	data = gdp_table_td[2].getText().split("   ")
	# print(data)
	subject = ""
	for d in data:
		if len(d) > 1:
			if d.startswith(' '):
				d = d[1:]
			if ":" in d and "." in d:
				# print(d)
				d1 = d.split(" ")
				# print(d1[0].replace(":", ""))
				# print(d1[1])
				dataJson[d1[0].replace(":", "")] = d1[1]
				continue
			d = d.replace(":", "")
			if "." not in d:
				subject = unidecode.unidecode(d).replace(" ", "").strip()
			else:
				dataJson[subject] = d
			# print(d)
	json_data = json.dumps(dataJson)
	# print(json_data)
	toan = -1
	nguvan = -1
	lichsu = -1
	diali = -1
	sinhhoc = -1
	hoahoc = -1
	vatli = -1
	gdcd = -1
	khtn = -1
	khxh = -1
	tiengAnh = -1

	if subject_list[0] in dataJson:
		toan = dataJson[subject_list[0]]

	if subject_list[1] in dataJson:
		nguvan = dataJson[subject_list[1]]

	if subject_list[2] in dataJson:
		lichsu = dataJson[subject_list[2]]

	if subject_list[3] in dataJson:
		vatli = dataJson[subject_list[3]]

	if subject_list[4] in dataJson:
		hoahoc = dataJson[subject_list[4]]

	if subject_list[5] in dataJson:
		diali = dataJson[subject_list[5]]

	if subject_list[6] in dataJson:
		sinhhoc = dataJson[subject_list[6]]

	if subject_list[7] in dataJson:
		gdcd = dataJson[subject_list[7]]

	if subject_list[8] in dataJson:
		khtn = dataJson[subject_list[8]]

	if subject_list[9] in dataJson:
		khxh = dataJson[subject_list[9]]

	if subject_list[10] in dataJson:
		tiengAnh = dataJson[subject_list[10]]

	ngaysinh = 0;
	thangsinh = 0;
	namsinh = 0;
	dataDay = gdp_table_td[1].getText().strip().split("/")
	if len(dataDay) > 2:
		ngaysinh = dataDay[0]
		thangsinh = dataDay[1]
		namsinh = dataDay[2]

	row_list.append([str(c), gdp_table_td[0].getText().strip(), ngaysinh, thangsinh, namsinh, toan, nguvan, lichsu, vatli, hoahoc, diali, sinhhoc, gdcd, khtn, khxh, tiengAnh])
	# student = Student(gdp_table_td[0].getText().strip(), gdp_table_td[1].getText().strip(), json_data)
	# print(student.toString())
	print('------------------')
	# break


with open('DiemThiTHPT2020HCM.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)