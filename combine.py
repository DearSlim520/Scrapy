# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import re
import csv
import sys

#cat *.csv>all.csv 或者 cat 1.csv 2.csv 3.csv...>all.csv 先通过cmd进入目录内，然后经过左边的指令合并多个csv为all
#数据预处理
#1. 删除多个第一行
#2. 删除多个不符合字符规范的行 —— 包含。:;/、都在typeSmall中归为其他类
#3. 删除detail列

df=pd.read_csv('/Users/hey/信息工程研究所/anquanke/安全客——！！！12.csv') 
df=df.astype(str)

#查找重复
#data1=df.drop_duplicates('name',keep=False)           #将有重复的全部去掉，保存到data1中
#print(data1)
#data2=df.drop_duplicates('name', keep='first')       #将有重复的只保留第一行，保存到data1中
#print(data2)
#data3=df.append(data1).drop_duplicates(keep=False)    #用全集减去没有重复的部分=有重复的部分的所有数据
#print(data3)
#y=data3.sort_values('name')                           #所有数据按照'name'排列
#print(y)
#data = y.to_csv("/Users/hey/right/文件/all_3.csv",index=0)        #保存为csv

#删除重复
#df.drop_duplicates('name', 'first', inplace=True)
#df = df.to_csv("/Users/hey/Desktop/楼宇办公自动化_nodup.csv",index=0)

#1. 删除标题行
#y=df[df['header'].str.contains('header')]  #显示出标题行
#print(y)
#df.drop(df.index[[27]],inplace=True)
#df = df.to_csv("/Users/hey/Desktop/楼宇办公自动化_nohead.csv",index=0)

#2. 规范行格式
'''
df.drop_duplicates('detail', 'first', inplace=True)
dele = df[df['detail'].str.contains('nan|漏洞细节尚未披露|删除标记')]
print(dele)
df.drop(df.index[[0,1,3]],inplace=True)
df.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——！！！2.csv",index=0)

'''
#df.loc[df['detail'].str.contains('管理系统|的程序|的软件|开源|平台|PHP|手机|应用程序|屏幕锁定|搜索引擎|浏览器|插件|网络系统|网络设备|玩具|编译器|模块|工具|Microsoft|套件|协议|控件|票务系统|移动设备|软件|编写|环境|玩具|media player|Software|解决方案|小程序|程序|WebWEB|游戏|钱包'), 'detail'] = '删除标记'
#首先，将含有物联网库类别名称关键字的
#df.loc[df['detail'].str.contains('CCD|CMOS|照相机|CPU|I/O|单元电源卡|OPC|服务器|PLC|POS|输入|RFID|RTU|SCADA|UPS|安防|按钮盒|半导体|背板|机架|编程软件|通信软件|编程电缆|编程软件|变频柜|变频器|变压器|工业PC|标记号|标记条|步进|操纵杆|操作面板|操作员站|测量光幕|称重模块|触摸屏|传感器|串口|存储卡|存储器|打印机|单板电脑|单元串联多电平|导线管|低压电器|电池|电磁阀|电动机|电动执行器|电机|电抗器|电缆|电流源型|电位器|电线|电压源型|电源|电子手轮|电子凸轮模块|定时器|定位模块|端子连接块|端子排|断路器|多点混合输入/输出卡|多点控制单元|多级切换机|阀门定位器|防雷浪涌保护|仿真模块|分布式接口|分布式控制系统|风机|风扇|蜂鸣器|复印机|高速布尔处理器|高速计数|工控|工业|工作站|功能站|光电|光端机|光伏|光源|互感器|滑轨|回路温度控制|机床|机器人|机械传动|激光检测|计时器|计数器|继电器|加固计算机|监测|减速机|交换机|接触器|接口模块|接入站点|接线端子|接线盒|解码器|开关|可控硅|控制电器|控制柜|控制器|冷却系统|离合器|连接电缆|连接器|连轴器|楼宇自动化|楼宇自控|路由器|滤波器|脉冲定位|脉冲量卡|脉冲输出|模拟量输|配电|启动器|起动器|前连接器|嵌入式|驱动板|驱动器|热电偶扩展|热电偶输|热电阻扩展|热电阻输|热交换系统|人机模块|扫描器|扫描机|扫描仪|摄像头|声光报警|时钟同步|视觉系统|视频管理平台|视频会议|视频监控|适配器|数控|数码显示单元|数字(离散)量输|数字量输|丝杠|伺服|锁存模块|条码识别|调节阀|调制解调器|通讯产品|通讯卡|通讯模块|图控一体化产品|图像采集卡|图像处理单元|网关|网络电话|网络机柜|网络视频服务器|网络通讯卡|微动开关|温度输入卡|温控|文本终端|无级变速器|无线接入点|无线通信|物联网|物流|现场总线|信号灯|信号隔离|信号转换|一体化驱动器|仪表|硬盘录像机|运动控制|自动化|增材|占位模块|整流模块|执行器|指示灯|制动单元|制动电阻|制动器|智能|中断模块|中继器|主控板|主令|转换器|总线电缆|通用电气')]
#df = df.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——！！！11.csv",index=0)

df.loc[df['detail'].str.contains('电子钱包'), 'detail'] = '删除标记'
df.drop_duplicates('detail', 'first', inplace=True)
a=df[df['detail'].str.contains('删除标记')]
print(a)
#df.drop(df.index[[12]],inplace=True)
#df = df.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——！！！13.csv",index=0)

#h = df.loc[df['detail'].str.contains('CCD|CMOS|照相机|CPU|I/O|单元电源卡|OPC|服务器|PLC|POS|输入|RFID|RTU|SCADA|UPS|安防|按钮盒|半导体|背板|机架|编程软件|通信软件|编程电缆|编程软件|变频柜|变频器|变压器|工业PC|标记号|标记条|步进|操纵杆|操作面板|操作员站|测量光幕|称重模块|触摸屏|传感器|串口|存储卡|存储器|打印机|单板电脑|单元串联多电平|导线管|低压电器|电池|电磁阀|电动机|电动执行器|电机|电抗器|电缆|电流源型|电位器|电线|电压源型|电源|电子手轮|电子凸轮模块|定时器|定位模块|端子连接块|端子排|断路器|多点混合输入/输出卡|多点控制单元|多级切换机|阀门定位器|防雷浪涌保护|仿真模块|分布式接口|分布式控制系统|风机|风扇|蜂鸣器|复印机|高速布尔处理器|高速计数|工控|工业|工作站|功能站|光电|光端机|光伏|光源|互感器|滑轨|回路温度控制|机床|机器人|机械传动|激光检测|计时器|计数器|继电器|加固计算机|监测|减速机|交换机|接触器|接口模块|接入站点|接线端子|接线盒|解码器|开关|可控硅|控制电器|控制柜|控制器|冷却系统|离合器|连接电缆|连接器|连轴器|楼宇自动化|楼宇自控|路由器|滤波器|脉冲定位|脉冲量卡|脉冲输出|模拟量输|配电|启动器|起动器|前连接器|嵌入式|驱动板|驱动器|热电偶扩展|热电偶输|热电阻扩展|热电阻输|热交换系统|人机模块|扫描器|扫描机|扫描仪|摄像头|声光报警|时钟同步|视觉系统|视频管理平台|视频会议|视频监控|适配器|数控|数码显示单元|数字(离散)量输|数字量输|丝杠|伺服|锁存模块|条码识别|调节阀|调制解调器|通讯产品|通讯卡|通讯模块|图控一体化产品|图像采集卡|图像处理单元|网关|网络电话|网络机柜|网络视频服务器|网络通讯卡|微动开关|温度输入卡|温控|文本终端|无级变速器|无线接入点|无线通信|物联网|物流|现场总线|信号灯|信号隔离|信号转换|一体化驱动器|仪表|硬盘录像机|运动控制|自动化|增材|占位模块|整流模块|执行器|指示灯|制动单元|制动电阻|制动器|智能|中断模块|中继器|主控板|主令|转换器|总线电缆|通用电气')]
#print(h)
#h.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——！！！12.csv",index=0)
#h = df.loc[df['detail'].str.contains('CCD|CMOS|照相机|CPU|I/O|单元电源卡|OPC|服务器|PLC|POS|RFID|RTU|SCADA|UPS|安防|按钮盒|半导体|编程软件|通信软件|编程电缆|编程软件|变频柜|变频器|变压器|工业PC|标记号|标记条|步进|操纵杆|操作面板|操作员站|测量光幕|称重模块|触摸屏|传感器|串口|存储卡|存储器|打印机|单板电脑|单元串联多电平|导线管|低压电器|电池|电磁阀|电动机|电动执行器|电机|电抗器|电缆|电流源型|电位器|电压源型|电源|电子手轮|电子凸轮模块|定时器|定位模块|端子连接块|端子排|断路器|多点|多级切换机|阀门定位器|防雷浪涌保护|仿真模块|分布式接口|分布式控制系统|风机|风扇|蜂鸣器|复印机|高速布尔处理器|高速计数|工控|工业|工作站|功能站|光电|光端机|光伏|光源|互感器|滑轨|回路温度控制|机床|机器人|机械传动|激光检测|计时器|计数器|继电器|加固计算机|监测|减速机|交换机|接触器|接口模块|接入站点|接线端子|接线盒|解码器|开关|可控硅|控制电器|控制柜|控制器|冷却系统|离合器|连接电缆|连接器|连轴器|楼宇自动化|楼宇自控|路由器|滤波器|脉冲定位|脉冲量卡|脉冲输出|模拟量输|配电|启动器|起动器|前连接器|嵌入式|驱动板|驱动器|热电偶扩展|热电偶输|热电阻扩展|热电阻输|热交换系统|人机模块|扫描器|扫描机|扫描仪|摄像头|声光报警|时钟同步|视觉系统|视频管理平台|视频会议|视频监控|适配器|数控|数码显示单元|数字(离散)量输|数字量输|丝杠|伺服|锁存模块|条码识别|调节阀|调制解调器|通讯产品|通讯卡|通讯模块|图控一体化产品|图像采集卡|图像处理单元|网关|网络电话|网络机柜|网络视频服务器|网络通讯卡|微动开关|温度输入卡|温控|文本终端|无级变速器|无线接入点|无线通信|物联网|物流|现场总线|信号灯|信号隔离|信号转换|一体化驱动器|仪表|硬盘录像机|运动控制|自动化|增材|占位模块|整流模块|执行器|指示灯|制动单元|制动电阻|制动器|智能|中断模块|中继器|主控板|主令|转换器|总线电缆|通用电气')]
#print(h)
#df = df.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——！！！5.csv",index=0)
#df = df.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——test!.csv",index=0)
'''
df = h.loc[df['detail'].str.contains('管理系统|的程序|的软件|开源|平台|PHP'), 'detail'] = '删除标记'
df.drop_duplicates('detail', 'first', inplace=True)
y=df[df['detail'].str.contains('删除标记')]
print(y)'''
#df.drop(df.index[[38]],inplace=True)
#df = df.to_csv("/Users/hey/信息工程研究所/anquanke/安全客——test!.csv",index=0)
#df.loc[df['typeSmall'].str.contains('。|：|；|/|、|，| |[0-9]|nan'), 'typeSmall'] = '其他'
#df.loc[df['typeSmall'].str.contains('nan'), 'typeSmall'] = '其他'
#df = df.to_csv("/Users/hey/Desktop/zol_SPJK/zol_SPJK/智能家居/智能家居2_formal.csv",index=0)

#3. 删除detail列
#df.drop(['typeMedium'],axis=1,inplace=True)
#df = df.to_csv("/Users/hey/Desktop/zol_SPJK/zol_SPJK/办公自动化系统/办公自动化系统_中关村在线_nodetail.csv",index=False,sep=',')

#4. 重命名
#df.rename(columns={'hah':'typeBig','typeBig':'typeMedium','typeMedium':'typeSmall','typeSmall':'typeSmallPlus'}, inplace = True)
#df.rename(columns={'dele':'typeSmallPlus'}, inplace = True)
#df = df.to_csv("/Users/hey/Desktop/zol_SPJK/zol_SPJK/视频监控/办公自动化系统_中关村在线_right.csv",index=0)

#5. 插入列/删除行
#df.insert(5,'typeSmallSmall','')
#df.drop(df.index[2652:2711],inplace=True)
#df = df.to_csv("/Users/hey/Desktop/楼宇办公自动化BOAS_2add.csv",index=0)
