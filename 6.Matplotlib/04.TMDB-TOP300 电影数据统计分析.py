"""
TMDB-TOP300 电影数据统计分析

分析流程：
准备工作：导入依赖库、配置运行时参数、创建子图完成基本布局、加载数据集
上映年份分析：统计 TOP300 影片中各年份上映电影数量变化，使用折线图可视化展示趋势
影片语言分析：统计并对比不同语言的电影数量，采用柱状图直观对比
电影类型分析：统计并对比不同题材类型的电影数量，使用柱状图呈现分布情况
评分分布分析：统计各区间电影评分占比情况，通过饼状图展示评分结构
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

from matplotlib.axes import Axes


def configure_chinese_font():
    """配置 matplotlib 中文字体，解决中文显示问题"""
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC', 'Heiti SC', 'STHeiti']


def create_figure():
    """创建画布和子图布局，返回画布对象和四个子图 Axes

    Returns:
        tuple: (figure, axes1, axes2, axes3, axes4)
    """
    figure, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)

    # 添加画布标题
    figure.suptitle('TMDB-TOP300 电影数据统计分析', fontsize=24, x=0.5, y=0.98)
    # 设置子图间距
    figure.subplots_adjust(hspace=0.5, wspace=0.3, top=0.92)

    axes1: Axes = axes[0][0]
    axes2: Axes = axes[0][1]
    axes3: Axes = axes[1][0]
    axes4: Axes = axes[1][1]

    return figure, axes1, axes2, axes3, axes4


def load_data(file_path: str) -> pd.DataFrame:
    """加载电影数据集

    Args:
        file_path: CSV 文件路径

    Returns:
        pd.DataFrame: 加载后的数据
    """
    data = pd.read_csv(
        file_path,
        nrows=30,
        usecols=['电影名', '电影年份', '上映时间', '电影类型', '电影时长', '用户评分', '语言'],
        dtype={
            '电影年份': 'Int64'
        }
    )
    return data


def plot_yearly_trend(data: pd.DataFrame, axes: Axes):
    """需求一：统计 TOP300 影片中各年份上映电影数量变化，使用折线图可视化展示趋势

    Args:
        data: 电影数据集
        axes: 子图 Axes 对象
    """
    # 1.1 缺失值处理：用上映时间的前4位填充缺失的电影年份
    data['电影年份'] = data['电影年份'].fillna(data['上映时间'].str[:4])

    # 1.2 分组统计每年电影数量
    year_count = data.groupby('电影年份')['电影年份'].count()

    # 1.3 组装数据
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = list(range(min_year, max_year + 1))
    y = [int(year_count.get(i, 0)) for i in x]

    # 1.4 绘制折线图
    axes.plot(x, y, color='green')
    axes.set_title('每年电影数量变化折线图', fontsize=18)
    axes.set_xlabel('年份', fontsize=14)
    axes.set_ylabel('电影数量', fontsize=14)
    axes.set_xticks(x[::8])
    axes.set_yticks(range(0, max(y) + 3, 3))  # 根据实际数据动态计算 y 轴刻度
    axes.grid(linestyle='--', alpha=0.5)


def plot_language_distribution(data: pd.DataFrame, axes: Axes):
    """需求二：统计并对比不同语言的电影数量，采用柱状图直观对比

    Args:
        data: 电影数据集
        axes: 子图 Axes 对象
    """
    # 2.1 获取不同语言对应的电影数量
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)

    x_language = language_count.index.tolist()
    y_language = language_count.values.tolist()

    # 2.2 绘制柱状图
    axes.bar(x_language, y_language, color='red', width=0.7)
    axes.set_title('不同语言电影数量柱状图', fontsize=18)
    axes.set_xlabel('语言', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.grid(linestyle='--', alpha=0.5)
    axes.tick_params(axis='x', rotation=45)


def plot_type_distribution(data: pd.DataFrame, axes: Axes):
    """需求三：统计并对比不同题材类型的电影数量，使用柱状图呈现分布情况

    Args:
        data: 电影数据集
        axes: 子图 Axes 对象
    """
    # 3.1 获取不同类型对应的电影数量（一部电影可能有多个类型）
    # 使用 explode 拆分逗号分隔的类型，再统计各类型数量
    type_count = data['电影类型'].str.split(',').explode().value_counts()

    # 3.2 绘制柱状图
    x_types = type_count.index.tolist()
    y_values = type_count.values.tolist()
    axes.bar(x_types, y_values, color='blue', width=0.7)
    axes.set_title('不同类型电影数量柱状图', fontsize=18)
    axes.set_xlabel('类型', fontsize=12)
    axes.set_ylabel('电影数量', fontsize=12)
    axes.grid(linestyle='--', alpha=0.5)
    axes.tick_params(axis='x', rotation=45)


def plot_score_distribution(data: pd.DataFrame, axes: Axes):
    """需求四：统计各区间电影评分占比情况，通过饼状图展示评分结构

    Args:
        data: 电影数据集
        axes: 子图 Axes 对象
    """
    # 4.1 获取各区间对应的电影数量
    score_count = data.groupby('用户评分')['用户评分'].count()

    # 合并小数据（比例小于5%）
    total = score_count.sum()
    large_scores: pd.Series = score_count.loc[score_count / total > 0.05].copy()
    small_scores: pd.Series = score_count.loc[score_count / total <= 0.05]

    # 如果有小数据，则合并到"其他"类别中
    if small_scores.shape[0] > 0:
        large_scores['其他'] = small_scores.sum()

    scores = large_scores.index.tolist()
    scores_values = large_scores.values.tolist()

    # 4.2 绘制饼状图
    axes.pie(scores_values, labels=scores, autopct='%1.1f%%',
             startangle=140, radius=1)
    axes.set_title('各区间电影评分占比饼状图', fontsize=18)
    axes.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.1))


def save_and_show(figure, save_path: str):
    """保存图片并展示

    Args:
        figure: 画布对象
        save_path: 图片保存路径
    """
    figure.savefig(save_path, dpi=100)
    plt.show()


def main():
    """主函数：TMDB-TOP300 电影数据统计分析"""
    # 获取脚本所在目录，确保路径正确
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'data', 'movie_list.csv')
    save_path = os.path.join(script_dir, 'data', 'movie_stats.png')

    # 准备工作
    configure_chinese_font()
    figure, axes1, axes2, axes3, axes4 = create_figure()
    data = load_data(data_path)

    # 执行四个分析任务
    plot_yearly_trend(data, axes1)
    plot_language_distribution(data, axes2)
    plot_type_distribution(data, axes3)
    plot_score_distribution(data, axes4)

    # 保存并展示
    save_and_show(figure, save_path)


if __name__ == '__main__':
    main()
