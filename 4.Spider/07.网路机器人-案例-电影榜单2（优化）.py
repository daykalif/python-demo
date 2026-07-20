import re

import requests
import csv
from lxml import html

# 常量
MOVIE_LIST_FILE = 'csv_data/movie_list2.csv'

TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL1 = "https://www.themoviedb.org/movie/top-rated"  # 高分电影榜单链接，默认展示第一页数据
TMDB_TOP_URL2 = "https://www.themoviedb.org/discover/movie/items"  # 高分电影榜单第二页链接


# 获取电影年份
def get_movie_year(movie_years):
    movie_year = movie_years[0].strip() if movie_years else ''
    return movie_year.replace('(', '').replace(')', '')


# 获取电影上映时间
def get_movie_publish_date(movie_release_dates):
    movie_publish_date = movie_release_dates[0].strip() if movie_release_dates else ''  # 2019-04-06 (CN)
    return re.search(r'(\d{4}-\d{2}-\d{2})', movie_publish_date).group()  # 2019-04-06


# 获取电影时长（统一转换为分钟，如：2h 20m ---> 140）
def get_movie_cost_time(movie_cost_times):
    movie_cost_time = movie_cost_times[0].strip() if movie_cost_times else ''  # 2h 20m / 40m / 2h
    h_res = re.search(r'(\d+)h', movie_cost_time)
    m_res = re.search(r'(\d+)m', movie_cost_time)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h * 60 + m


# 获取电影详情
def get_movie_info(movie_info_url):
    # 1.发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url, timeout=60)
    print(f"发送请求{movie_info_url}，获取电影详情数据...")

    # 2.解析数据，获取电影详情
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    # 电影年份
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    # 上映时间
    movie_release_dates = movie_doc.xpath(
        "//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    # 电影类型（标签）
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    # 电影时长
    movie_cost_times = movie_doc.xpath(
        "//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    # 用户评分
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    # 语言
    movie_language = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    # 导演
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    # 作者
    movie_authors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    # 宣传标语
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    # 简介
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    # 3.返回电影详情 - 字典
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "电影年份": get_movie_year(movie_years),
        "上映时间": get_movie_publish_date(movie_release_dates),
        "电影类型": ','.join(movie_tags) if movie_tags else '',
        "电影时长": get_movie_cost_time(movie_cost_times),
        "用户评分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_language[0].strip() if movie_language else '',
        "导演": ','.join(movie_directors) if movie_directors else '',
        "作者": ','.join(movie_authors) if movie_authors else '',
        "宣传标语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else ''
    }
    return movie_info


# 保存电影数据，保存为csv文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        # 定义表头字段
        fieldnames = ['电影名', '电影年份', '上映时间', '电影类型', '电影时长', '用户评分', '语言', '导演', '作者',
                      '宣传标语', '简介']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # 自动写入表头行
        writer.writeheader()
        # 写入电影数据
        for movie in all_movies:
            writer.writerow(movie)


# 主函数
def main():
    # 保存所有电影数据
    all_movies = []

    for page_num in range(1, 6):  # 从第一页到第5页
        # 1.发送请求获取高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL1, timeout=60)
        else:
            response = requests.post(
                TMDB_TOP_URL2,
                f'air_date.gte=&air_date.lte=&certification=&certification_country=US&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-01-20&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=US&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400'
                , timeout=60
            )
        print(f"发送请求，访问第{page_num}页的数据，获取TMDB电影榜单数据...")

        # 2.解析数据，获取电影列表
        document = html.fromstring(response.text)
        moive_list = document.xpath(
            f"//*[@id='page_{page_num}']/div/div/div[@class='comp:poster-card w-full bg-white border border-light-grey hover:border-gray-300 rounded-lg shadow-sm overflow-hidden']")

        # 3.遍历电影列表，获取电影详情
        for movie in moive_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                # 电影详情的url地址
                movie_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影详情数据
                movie_info = get_movie_info(movie_url)
                all_movies.append(movie_info)

    # 4.保存数据，保存为csv文件
    print("获取到所有电影的电影详情，保存电影数据到csv文件...")
    save_all_movies(all_movies)


if __name__ == '__main__':
    main()
