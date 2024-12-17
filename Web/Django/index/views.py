# Create your views here.
from django.shortcuts import render  # 导入render模块
from index.models import events

# 先定义一个数据列表，当然后面熟了可以从数据库里取出来
list1 = [{'title': '习近平会见主要国际经济组织负责人', 'value': '20000123'},
        {'title': '尹锡悦等8人被列入逮捕名单', 'value': ' 1188935'},
        {'title': '谢娜是乐华的第一个艺人', 'value': '1029589'},
        {'title': '2025年财政和货币政策有哪些变化', 'value': ' 725440'},
        {'title': 'TGA2024投票最后一天', 'value': ' 720001 '},
        {'title': '黑神话悟空更新', 'value': ' 715045'},
        {'title': '老人退休工资2800却花150万买保险', 'value': ' 640588'},
        {'title': '双轨 换角', 'value': '608894'},
        {'title': '年前减肥最后的希望', 'value': ' 620001'},
        {'title': '谢娜没去陈乔恩婚礼的原因', 'value': '583602'},
        {'title': '藏海传', 'value': '566986'},
        {'title': '女子为逃避欠款自导自演丢了10万', 'value': ' 498563'},
        {'title': '盲道不仅要指路更要保障盲人安全', 'value': ' 453701'},
        {'title': '严浩翔新歌疑似抄袭', 'value': '451196'},
        {'title': '迪丽热巴方确认不参加星光大赏', 'value': '450644'},
        {'title': '泽连斯基曝光乌军死亡人数', 'value': ' 445990'},
        {'title': '双轨男主', 'value': '438199'},
        {'title': '替父母越界养老的年轻人该何去何从', 'value': ' 425679'},
        {'title': '一块吧唧被炒到7万多背后', 'value': ' 420687'},
        {'title': '理发师晓华谈到孩子差点儿落泪', 'value': ' 300974'}]


def index(request):
        for news in list1:
                events.objects.create(title=news['title'], value=news['value'])
        list = events.objects.all()
        return render(request, 'index.html', {'form': list})
