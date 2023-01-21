import re

html_str = """
<div class="col-md-3" style="display: flex; flex-direction: column; padding-top: 15px; padding-bottom: 15px;">
    <div class="course-item">
        <a href="#">
            <div style="background-color: rgb(255, 255, 255); border-radius: 5px;">
                <div>
                    <img src="https://dev-img-static.walkclass.com/course_rescourses/20200421/384b1b5ae0d749ed880b14a975d69c4e.jpg" class="coverImg">
                </div>
                <div style="display: flex; flex-direction: column; color: rgb(153, 153, 153); position: relative; padding: 0px 10px;">
                    <div class="row" style="margin: 5px 0px;">
                        <p style="font-size: 18px; color: rgb(102, 102, 102); margin: 0px;">这个用来课程广场吧</p>
                    </div>
                    <div class="row" style="margin: 5px 0px;">
                        <div style="float: left;"><span style="width: 120px;">主讲人</span> :<span>好的</span>
                        </div>
                        <div style="float: right;"><span style="color: red; margin-right: 5px;">¥0</span><span style="text-decoration: line-through; color: rgb(204, 204, 204);">¥9999.99</span>
                        </div>
                    </div>
                </div>
                <p class="desc">简介：<span>撒地方何时放假几时放假自己曾经在家吃饺子长久之计财政局参加自出机杼韭菜饺子鸡翅走开走开这款裤子看</span>
                </p>
                <div style="overflow: hidden; font-size: 14px; padding: 0px 10px 10px;">
                    <button class="btn btn-danger btn-xs">下架课程</button> <span style="float: right;"><span>40</span>人参与学习</span>
                </div>
            </div>
        </a>
    </div>
</div>
"""

re.sub(r"<[^>]*>|\s|&nbsp;", "", html_str)  # [^>] 除了又括号

re.sub(r"<.*?>", "", html_str)

s = "This is a number 234-432-33-673"
re.match(r".*(\d{3}\d{3}|d{2}|d{3})", s).group(1)  # 234-432-33-673
re.match(r".*(\d+\d+|d+|d+)", s).group(1)  # 4-432-33-673
re.match(r".*?(\d+\d+|d+|d+)", s).group(1)  # 234-432-33-673

re.search(r"https://.*?\.jpg", html_str).group()    # 加?表示非贪婪
