# -*- coding: utf-8 -*-
import datetime
import sys
import re
import requests


BAR_CAPACITY = 50
FORMATTER = '%a, %d %b %Y %H:%M:%S (GMT)'


def get_top_followers():
	headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
	# followers = []
	# page = requests.get('https://api.github.com/users/LikaiLee/followers?page=0&per_page=100', headers=headers).json()
	# for follower in page:
	# 	follower_info = requests.get(follower['url'], headers=headers).json()
	# 	followers.append({
	# 		'login': follower_info['login'],
	# 		'name': follower_info['name'] if follower_info['name'] else follower_info['login'],
	# 		'avatar_url': follower_info['avatar_url'],
	# 		'home': follower_info['html_url']
	# 	})
	# followers = followers[::-1]
	followers = [{'login': 'VXenomac', 'name': 'VXenomac', 'avatar_url': 'https://avatars1.githubusercontent.com/u/21958044?v=4', 'home': 'https://github.com/VXenomac'}, {'login': 'SiwenZheng', 'name': 'SiwenZheng', 'avatar_url': 'https://avatars0.githubusercontent.com/u/16337571?v=4', 'home': 'https://github.com/SiwenZheng'}, {'login': 'Lafido', 'name': 'Zhi Li', 'avatar_url': 'https://avatars2.githubusercontent.com/u/2927304?v=4', 'home': 'https://github.com/Lafido'}, {'login': 'limingLiu-708', 'name': 'limingLiu-708', 'avatar_url': 'https://avatars1.githubusercontent.com/u/49385193?v=4', 'home': 'https://github.com/limingLiu-708'}, {'login': 'ztygalaxy', 'name': '张天宇', 'avatar_url': 'https://avatars2.githubusercontent.com/u/35124692?v=4', 'home': 'https://github.com/ztygalaxy'}, {'login': 'MC01DA', 'name': 'Jerffelly', 'avatar_url': 'https://avatars1.githubusercontent.com/u/30335051?v=4', 'home': 'https://github.com/MC01DA'}, {'login': 'MQQM', 'name': 'Tianhao Zhang', 'avatar_url': 'https://avatars3.githubusercontent.com/u/34396349?v=4', 'home': 'https://github.com/MQQM'}, {'login': 'jsjzyzc', 'name': 'Aniu', 'avatar_url': 'https://avatars3.githubusercontent.com/u/32808240?v=4', 'home': 'https://github.com/jsjzyzc'}, {'login': 'Ruil1n', 'name': 'Ruil1n', 'avatar_url': 'https://avatars1.githubusercontent.com/u/29536370?v=4', 'home': 'https://github.com/Ruil1n'}, {'login': 'GyanH', 'name': 'GyanH', 'avatar_url': 'https://avatars0.githubusercontent.com/u/34931039?v=4', 'home': 'https://github.com/GyanH'}, {'login': 'Outside-man', 'name': 'dango', 'avatar_url': 'https://avatars1.githubusercontent.com/u/19770588?v=4', 'home': 'https://github.com/Outside-man'}, {'login': 'heyongpeng', 'name': 'heyongpeng', 'avatar_url': 'https://avatars0.githubusercontent.com/u/26265667?v=4', 'home': 'https://github.com/heyongpeng'}, {'login': 'colla2me', 'name': 'Harimoto Satoshi', 'avatar_url': 'https://avatars2.githubusercontent.com/u/26298112?v=4', 'home': 'https://github.com/colla2me'}]
	html = '<table>\n'
	for i in range(min(len(followers), 14)):
		login = followers[i]['login']
		name = followers[i]['name']
		avatar_url = followers[i]['avatar_url']
		home = followers[i]['home']
		if i % 7 == 0:
			if i != 0:
				html += '</tr>\n'
			html += '<tr>\n'
		html += f'''    <td align="center">
      <a href="{home}">
        <img src="{avatar_url}" width="100px;" alt="{login}"/>
      </a>
      <br />
      <a href="{home}">{name}</a>
    </td>'''
	html += '</tr>\n</table>'
	return html


def get_past_percentage(cur_year, now):
	start_of_year = datetime.datetime(cur_year, 1, 1)
	end_of_year = datetime.datetime(cur_year + 1, 1, 1)
	return (now - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()


def gen_progress_bar(capacity, percent):
	bar = int(capacity * percent)
	return ''.join(['░' if i > bar else '█' for i in range(capacity)])

if __name__ == '__main__':
	assert(len(sys.argv) == 2)
	readme_path = sys.argv[1]
	cur_year = datetime.datetime.now().year
	now = datetime.datetime.now()
	update_time = now.strftime(FORMATTER)
	# get percentage
	percent = get_past_percentage(cur_year, now)
	# generate progress bar according to percentage
	progress_bar = gen_progress_bar(BAR_CAPACITY, percent)
	# get followers
	followers = get_top_followers()
	
	with open(readme_path, 'r') as readme:
		content = readme.read()
	content = re.sub(r"(?<=<!\-\-START_SECTION:cur\-year\-\->)[\s\S]*(?=<!\-\-END_SECTION:cur\-year\-\->)", f'{cur_year}', content)
	content = re.sub(r"(?<=<!\-\-START_SECTION:year\-progress\-bar\-\->)[\s\S]*(?=<!\-\-END_SECTION:year\-progress\-bar\-\->)", f'{progress_bar}', content)
	content = re.sub(r"(?<=<!\-\-START_SECTION:year\-progress\-percent\-\->)[\s\S]*(?=<!\-\-END_SECTION:year\-progress\-percent\-\->)", f'{round(percent * 100, 2)}', content)
	content = re.sub(r"(?<=<!\-\-START_SECTION:top\-followers\-\->)[\s\S]*(?=<!\-\-END_SECTION:top\-followers\-\->)", f'\n{followers}\n', content)
	content = re.sub(r"(?<=<!\-\-START_SECTION:update\-time\-\->)[\s\S]*(?=<!\-\-END_SECTION:update\-time\-\->)", f'{update_time}', content)
	with open(readme_path, 'w') as readme:
		readme.write(content)
