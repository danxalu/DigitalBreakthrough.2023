from bs4 import BeautifulSoup
import requests
import json
import aiohttp
import asyncio

import pandas as pd
import csv


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.34"
    }

global data
data = {}


async def get_page_data(session, resource, statistics, req_kpi_list, scr, tag, main_class, child_cond_tag = '', child_cond_class = ''):
    url = None
    if statistics == "yt-sb": #url текущей страницы
        url = "https://socialblade.com/youtube/channel/"+resource
    elif statistics == "tg-tgstat":
        url = "https://tgstat.ru/channel/"+resource+"/stat"
        
    try:
        async with session.get(url=url, headers=headers) as response:
            response_text = await response.text() #получаем содердимое страницы
            soup = BeautifulSoup(response_text, 'html.parser')
                
            for req_kpi in req_kpi_list:
                if statistics == "yt-sb":
                    if req_kpi == "subs":
                        kpi = soup.find_all("span", {"id": "youtube-stats-header-subs"})
                    elif req_kpi == "views_month":
                        kpi = soup.find_all("p", {"style": "font-size: 1.4em; color:#666; font-weight: 600; padding-top: 14px; padding-left: 30px; text-align: center;"})
                    current_str = kpi[0].text.strip().split(" ")[0] #выделяем 
                    data[req_kpi]=current_str
                elif statistics == "tg-tgstat":
                    if req_kpi == "err":
                        kpi = soup.find_all("b", {"class": "text-dark mr-2"})
                        current_str = kpi[3].text.strip().split(" ")[0]
                        data[req_kpi]=current_str
    except BaseException:
        for req_kpi in req_kpi_list:
            data[req_kpi] = None
        
            

async def gather_data(resource, statistics, kpi, scr, tag, main_class, parent_cond_tag = '', parent_cond_class = ''): #сбор новостей
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_page_data(session, resource, statistics, kpi, scr, tag, main_class, parent_cond_tag, parent_cond_class))]
        await asyncio.gather(*tasks)
        

def parse(resource, statistics, kpi, scr = None, tag =None, main_class =None, parent_cond_tag = None, parent_cond_class = None): #функция запуска парсинга
    asyncio.run(gather_data(resource, statistics, kpi, scr, tag, main_class, parent_cond_tag, parent_cond_class))
    

def to_json(bases, name_file): #экспорт в json
    with open("{0}.json".format(name_file), "w", encoding='utf-8') as file:
        json.dump(bases, file, indent=4, ensure_ascii=False)


def read_write_file(filename_r="nicknames.csv", filename_w="statistics.csv"):
    nicks = []
    with open(filename_r, 'r', newline='') as csvfile_r:
        reader = csv.DictReader(csvfile_r)
        for row in reader:
            nicks.append(str(row["nickname"]))
    print(nicks)

    with open(filename_w, 'w', newline='') as csvfile_w:
        fieldnames = ['nickname', 'tg-err', 'yt-subs', 'yt-views-month']
        writer = csv.DictWriter(csvfile_w, fieldnames=fieldnames)
        writer.writeheader()
        for nickname in nicks:
            global data
            data = {}
            parse(nickname, 'tg-tgstat', ["err"])
            parse(nickname, 'yt-sb', ["subs", "views_month"])
            for x in data:
                if data[x] == "--":
                    data[x] = 0
            print(data)
            tg_err = data["err"]
            yt_subs = data["subs"]
            yt_views_month = data["views_month"]
            
            writer.writerow({'nickname': nickname, 'tg-err': tg_err, 'yt-subs': yt_subs, 'yt-views-month': yt_views_month})

    excel_file = pd.read_csv(filename_w)
    excel_file.to_excel('statistics.xlsx', index=None, header=True)
          
        
if __name__ == '__main__':
    read_write_file()





    
