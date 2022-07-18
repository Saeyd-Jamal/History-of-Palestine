# import models
from flask import Flask, request, render_template
import pandas as pd
import news

# أسم المشروع
history_ps = Flask(__name__)

# أمر لتشغل القراءة المتعددة في الدوال
history_ps.jinja_env.filters['zip'] = zip

# الصفحة الرئيسية
@history_ps.route('/')
def home_page():
  return render_template('index.html' , title_page ='Home')


# الأحداث
@history_ps.route('/events')
def events_page():
  data_events = pd.read_csv('static/research/events.csv', encoding = "cp720")
  # print(data_events['text'])
  list_year = list(set(data_events['year']))
  list_year.sort()
  num_year_events = len(list_year)
  num_events_10 = 1
  num_events_10 += int(format(num_year_events / 10, '.0f' ))
  link_nam = []
  for link,date in zip(data_events['Link'],data_events['date']):
    link = str(link)
    link = link.replace("/", "")
    link = link.replace(":", "")
    link = link.replace(".", "")
    link = link.replace("%", "")
    link = link.replace("?", "")
    link = link.replace("=", "")
    link = link.replace("#", "")
    link = link.replace("(", "")
    link = link.replace(")", "")
    date = date.replace("/", "")
    date = date.replace(",", "")
    link_nam.append(link + date)
  return render_template('events.html',
                        title_page ='Events',
                        style_css= 'events.css',
                        data_events = data_events,
                        list_year=list_year,
                        num_year_events = num_year_events,
                        num_events_10 =num_events_10,
                        links_nam =link_nam
                        )

# الأخبار
@history_ps.route('/news')
def news_page():
  new = []
  # غزة الأن
  gazaAlan = {}
  news.gazaAlanFun(gazaAlan)
  # الجزيرة
  aljazeera = {}
  news.aljazeeraFun(aljazeera)
  # دنيا الوطن
  alwatan = {}
  news.alwatanFun(alwatan)
  # معا
  maannews = {}
  news.maannewsFun(maannews)
  # القدس برس
  qudspress ={}
  news.qudspressFun(qudspress)
  new.append(gazaAlan)
  new.append(aljazeera)
  new.append(alwatan)
  new.append(maannews)
  new.append(qudspress)
  return render_template('news.html',title_page ='News',news = new)

# الابطال
@history_ps.route('/heroes')
def heroes_page():
  data_heroes = pd.read_csv('static/research/heroes.csv', encoding = "cp720")
  num_row_heroes = 1
  num_con_heroes = 1
  num_heroes = len(data_heroes['name'])
  num_row_heroes += int(format(num_heroes / 4, '.0f' ))
  num_con_heroes += int(format(num_heroes / 8, '.0f' ))
  return render_template('heroes.html' , 
                        title_page ='Heroes',
                        data_heroes = data_heroes,
                        num_row_heroes = num_row_heroes,
                        num_con_heroes = num_con_heroes,
                        num_heroes = num_heroes
                        )

# البحث في الأبطال
@history_ps.route('/heroes_search', methods=['POST'])
def heroes_page_search():
  data_heroes = pd.read_csv('static/research/heroes.csv', encoding = "cp720")
  search_hero = request.form['search']
  name_s = ''
  work_s = ''
  link_s = ''
  img_name_s = ''
  for name,work,link,img_name in zip(data_heroes['name'],data_heroes['work'],data_heroes['link'],data_heroes['img_name']):
    if name == search_hero:
      name_s = name
      work_s = work
      link_s = link
      img_name_s = str(img_name)
      break;
  return render_template('heroes.html',
                          title_page ='Heroes',
                          search = 'yes',
                          name_sh = name_s,
                          work_sh = work_s,
                          link_sh = link_s,
                          img_name_sh = img_name_s,
                          )

# المدن
@history_ps.route('/cities')
def cities_page():
  data_cities = pd.read_csv('static/research/cities.csv', encoding = "cp720")
  return render_template('cities.html' , title_page ='Cities', data_cities = data_cities)

# run app
if __name__ == "__main__":
  history_ps.run(debug=True)