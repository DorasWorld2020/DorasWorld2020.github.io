# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 08/08/2021 09:17
# @Author  : Xueli
# @File    : lizhi.py.py
# @Software: PyCharm

import argparse
import requests
import re
import time
import subprocess
import pandas as pd
from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry



def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


parser = argparse.ArgumentParser()
parser.add_argument(
    '-id', '--liveid', dest='liveid', type=str, required=True,
    help='The liveid of the lizhi host'
)
parser.add_argument(
    '-c', '--count-only', dest='count_only', action='store_true',
    help='Only inform the count of messages.'
)
args = parser.parse_args()


liveid = args.liveid
# 添加头部信息，伪装手机浏览器访问该URL
header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
msg_time = int(time.time() * 1000)

session = requests.Session()
# session.keep_alive = False
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', HTTPAdapter(max_retries=50))
session.mount('https://', HTTPAdapter(max_retries=50))

while True:
    # time.sleep(5)
    url=f"https://appweb.lizhi.fm/live/comments?liveId={liveid}&start={msg_time}&count=50"
    # print(url)
    # res = requests.get(url,headers=header)
    res = session.get(url, headers = header, timeout = 5)
    try:
        # print('starting reading comments')
        json_res = res.json()
        # print('finished reading comments')
    except Exception as e:
        print(f"Failed to read comments: {e}")
        # print(res.text)
        continue

    msg_time = json_res['comments']['end']
    msg_count = len(json_res['comments']['list'])

    # 整点报时
    local_dt = time.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        if local_dt[14:16] == '00':
            if local_dt[17:19] == '00':
                print('整点报时' + local_dt)
                welcome_msg = f"小管家滴滴报时，宜家系多肉时间 {local_dt} 秒，欢迎大家来到多肉的世界。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，现在是多肉时间 {local_dt} ，欢迎大家来到多肉的世界, 爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！ "
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                break
            if local_dt[17:19] == '01':
                print('整点报时' + local_dt)
                welcome_msg = f"小管家滴滴报时，宜家系多肉时间 {local_dt} 秒，欢迎大家来到多肉的世界。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，现在是多肉时间 {local_dt}，欢迎大家来到多肉的世界, 爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！ "
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                break
            if local_dt[17:19] == '02':
                print('整点报时' + local_dt)
                welcome_msg = f"小管家滴滴报时，宜家系多肉时间 {local_dt} 秒，欢迎大家来到多肉的世界。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，现在是多肉时间 {local_dt}，欢迎大家来到多肉的世界, 爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！ "
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                break
            if local_dt[17:19] == '03':
                print('整点报时' + local_dt)
                welcome_msg = f"小管家滴滴报时，宜家系多肉时间 {local_dt} 秒，欢迎大家来到多肉的世界。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，现在是多肉时间 {local_dt}，欢迎大家来到多肉的世界, 爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！ "
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                break
            if local_dt[17:19] == '04':
                print('整点报时' + local_dt)
                welcome_msg = f"小管家滴滴报时，宜家系多肉时间 {local_dt} 秒，欢迎大家来到多肉的世界。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，现在是多肉时间 {local_dt}，欢迎大家来到多肉的世界, 爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！ "
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                break
            if local_dt[17:19] == '05':
                print('整点报时' + local_dt)
                welcome_msg = f"小管家滴滴报时，宜家系多肉时间 {local_dt} 秒，欢迎大家来到多肉的世界。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，现在是多肉时间 {local_dt}，欢迎大家来到多肉的世界, 爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！ "
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                break
            break
        else:
            break


    # 播报弹幕数
    if args.count_only and msg_count > 0:
        speak_msg = f"你收到了 {msg_count} 条消息."
        cmd = ["say", "-v", "Ting-Ting", "-r", "250", speak_msg]
        subprocess.call(cmd)

    # 播报弹幕内容
    else:
        # 从服务器返回的json对象获取每一条弹幕消息，并按照不同的规则“播报”弹幕消息
        for msg in json_res['comments']['list']:
            # 获取每一条弹幕消息的用户名和弹幕内容
            user_name = deEmojify(msg['userName'])
            if not user_name.strip():
                user_name = f"{user_name} 个空白"
            comment = msg['comment']

            # 给多肉号船员换个昵称
            name_df = pd.read_csv('nickname.csv', header = 0)
            nickname = name_df.set_index('name')['nick_name'].to_dict()
            for k,v in nickname.items():
                if k in user_name:
                    user_name = v

            # 定义弹幕消息的播报内容
            speak_msg = f"{user_name} 说: {comment}"

            # 欢迎多肉号成员回家
            if user_name in nickname.values() and speak_msg.__contains__('欢迎'):
                welcome_msg = f"小管家欢迎 {user_name} " \
                              f"回到多肉号。小管家温馨提醒，大家每天要睡饱饱，吃好好！。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                time_msg = time.asctime()
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家欢迎 {user_name} " \
                              f"返来多肉号。小管家温馨提醒，大家每天要睡饱饱，吃好好！。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break

            # 欢迎过客来到多肉的世界
            if speak_msg.__contains__('欢迎'):
                welcome_msg = f"小管家欢迎 {user_name} 来到多肉的世界"
                custom_msg = f"{user_name} " \
                             f"你好哇！小管家温馨提醒，大家每天要睡饱饱，吃好好！。爱尔兰作家奥斯卡·王尔德说，爱自己是终身浪漫的开始。To love oneself is the beginning of a lifelong romance。小管家衷心希望大家新的一周继续认真生活，好好爱自己唷！！"
                time_msg = time.asctime()
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", custom_msg]
                subprocess.call(cmd)
                break

            # 过滤弹幕消息，如果弹幕中包含以下词汇，则忽略此条弹幕
            filter_ls = ['恭喜', '系统提示', '鲜花', '送了']
            if any (word in speak_msg for word in filter_ls):
                print('不播报此条消息: ' + speak_msg)
                break

            # 用不同的语言（方言）播放对应的弹幕消息
            if speak_msg.__contains__('!cantonese'):
                speak_msg = speak_msg.replace("!cantonese", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", speak_msg]
                subprocess.call(cmd)
                # auto_msg = f"你好哇。咸鱼多肉宜家唔得闲！我系多肉既小管家，你有咩事可以同我讲，我帮你转达。如果唔想听哩一条自动回复，可以睇下公告既命令说明。得闲再一起玩啦！"
                # time.sleep(2)
                # cmd = ["say", "-v", "Sin-ji", "-r", "200", auto_msg]
                # subprocess.call(cmd)
                break

            if speak_msg.__contains__('!japanese'):
                speak_msg = f"{user_name} 说: {comment}"
                speak_msg = speak_msg.replace("!japanese", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Kyoko", "-r", "200", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!english'):
                speak_msg = f"{comment}"
                speak_msg = speak_msg.replace("!english", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Victoria", "-r", "185", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!korean'):
                speak_msg = speak_msg.replace("!korean", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Yuna", "-r", "180", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!dutch'):
                speak_msg = speak_msg.replace("!dutch", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Xander", "-r", "200", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!german'):
                speak_msg = speak_msg.replace("!german", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Anna", "-r", "190", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!french'):
                speak_msg = speak_msg.replace("!french", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Thomas", "-r", "185", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!spanish'):
                speak_msg = speak_msg.replace("!spanish", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Monica", "-r", "190", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!cnoff'):
                speak_msg = speak_msg.replace("!cnoff", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "195", speak_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('!hkoff'):
                speak_msg = speak_msg.replace("!hkoff", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", speak_msg]
                subprocess.call(cmd)
                break
            if speak_msg.__contains__('!readoff'):
                speak_msg = speak_msg.replace("!readoff", " ")
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                break

            else:
                time_msg = time.asctime()
                print(time_msg,speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "200", speak_msg]
                subprocess.call(cmd)
                # auto_msg = f"你好哇，咸鱼多肉在忙其他事情啦！我是勤快的小管家，有事可以和我讲。虽然现在我笨笨的，可是我在很努力学习啦！不要嫌弃我诶。希望咸鱼多肉早点翻身，让我多学一点技能，和大家愉快玩耍。友情提示，如果不想听到小管家的自动回复，可以查看公告的操作命令哦"
                # time.sleep(2)
                # cmd = ["say", "-v", "Mei-Jia", "-r", "200", auto_msg]
                # subprocess.call(cmd)