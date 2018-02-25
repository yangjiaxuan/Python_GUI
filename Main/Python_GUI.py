
#encoding: utf-8

import tkinter as tk


window = tk.Tk()

# 标题
window.title('GUI')

windowW = 400
windowH = 400
window.geometry('%dx%d'%(windowW, windowH))



def cancleAction():
	print("cancleAction")
	pass

def sureAction():
	print("sureAction")
	pass

def returnAction():
	print("ReturnAction")
	pass

width  = 5
height = 5
padding = 50

textTF     = tk.Text(window, height=3, bg='white',fg='black')
cancle_btn = tk.Button(window, text='取消', command=cancleAction, width=width, height=height, bg='yellow')
sure_btn   = tk.Button(window, text='确认', command=sureAction, width=width, height=height, bg='red')

# 使用grid布局
# row: 单元格坐标X
# column: 单元格坐标Y
# rowspan：竖直方向占用格子数     columnspan：水平方向占用格子数 
# padx:水平方向外边距   pady:竖直方向外边距   
# ipadx:水平方向内边距  ipady:竖直方向内边距 
# sticky: 控件的对齐方式 N:上对齐 W:左对齐 S:向下填充 E:向右填充    
# grid()将窗口看做一张表格，将控件放在其中的单元格中，而row、column则用来设置控件所在单元格的坐标。

# cancle_btn.grid(row=0, column=0, padx=padding, pady=padding,rowspan=1, columnspan=1)
# sure_btn.grid(row=0, column=1, padx=padding, pady=padding, rowspan=1, columnspan=1, sticky='E')


# place 绝对位置布局
# x,y: 从横的绝对位置  width:宽 height:高
# anchor: 锚点的位置，指定某个位置的绝对值坐标为x,y eg: sw 左下角的绝对值坐标为x,y
#  nw    n    ne
#  w   center  e
#  sw    s    se

# cancle_btn.place(x=padding, y=(windowH-padding), anchor='sw')
# sure_btn.place(x=(windowW-padding), y=(windowH-padding), anchor='se')

# relx, rely: 相对的坐标 值：0~1
# 可以同时使用相对坐标和绝对坐标，此时先根据相对坐标确定控件位置，
# 然后根据绝对坐标使控件进行偏移，最后确定控件的最终位置。
textTF.place(x=0, y=padding, relx=0.5, rely=0, width=(windowW-2*padding), height=(windowH-4*padding), anchor='n')
# textTF.focus_set()
textTF.bind('<Return>',returnAction)
cancle_btn.place(x=-padding, y=padding, relx=0.25, rely=0.85,anchor='sw')
sure_btn.place(x=padding, y=padding, relx=0.75, rely=0.85, anchor='se')


# pack 将小部件放置到主窗口中
# side:'top'、'bottom'、'left'、'right'，
#      分别表示将控件位置设在窗口顶部中心、底部中心、左边中心、右边中心。
#      side默认值为'top'。
# padx、pady、ipadx、ipady: 分别设置控件水平方向外边距、竖直方向外边距、水平方向内边距、竖直方向内边距。
# fill:'none'、'x'、'y'、'both'。
#      分别表示不填充、将控件沿水平方向填充、将控件沿竖直方向填充、将控件沿水平和竖直方法填充。
# expand:有两个可选值：0、1（或者'yes'、'no'）。expand默认值为0。
#        当expand属性为0时，前面所说的side、fill一切正常；
#        当expand属性为1时，side属性无效，此时控件会在窗口中心位置，
#        且fill既可沿水平方向填充，也可沿竖直方向填充。
# cancle_btn.pack(side='top', padx=5, pady=5, ipadx=5, ipady=5, fill='none', expand='yes')
# sure_btn.pack(side='top', padx=5, pady=5, ipadx=5, ipady=5, fill='none', expand='yes')


# 消息循环
window.mainloop()






