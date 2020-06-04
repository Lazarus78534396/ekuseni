from kivymd.app import MDApp
import requests
from bs4 import BeautifulSoup
from kivymd.uix.list import OneLineListItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
class MainApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Blue"

	def on_start(self):
		url = "http://www.times.co.sz"
		response = requests.get(url)

		soup = BeautifulSoup(response.content, 'html5lib')
		headlines = []

		table = soup.find('div', attrs = {'id':'more_news_index'})
		for row in table.findAll('h2'):
			temp = row.text
			headlines.append(temp)
		
		for headline in headlines:
			self.root.ids.container.add_widget(
				OneLineListItem(text=headline,))

	
				
MainApp().run()