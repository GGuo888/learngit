import time
from info import infos
from film_selector import FilmSelect
from seat_book import SeatBooking

class Controller:
    def __init__(self,films):
        self.films = films # 电影库所有的电影
        # 打印欢迎语
        self.welcome()
        # 用户选择想观看的电影
        self.choose_film()
        # 根据用户的选择，执行不同的流程
        if self.choice != 'x':
            # 为指定场次预定座位
            self.choose_seat()
        # 打印结束语
        self.bye()

    # 用户选择想观看的电影
    def choose_film(self):
        # 实例化Filmselector类
        selector = FilmSelect()
        # 展示所有可选择的电影
        selector.display_options(self.films)
        # 通过get_choice()方法获取用户的选择
        self.choice = selector.get_choice(self.films)

    # 为指定场次预定座位
    def choose_seat(self):
        # 取出用户选择的电影
        film = self.films[int(self.choice)-1]
        # 取出所选择的电影的电影名，座位表，宣传画
        name = film['name']
        seats_list = film['seats']
        symbol = film['symbol']

        # 打印提示信息和电影宣传画
        print('正在为您预定电影《{}》的座位...'.format(name))
        time.sleep(0.7)
        print(symbol)
        time.sleep(0.7)

        # 打印预定座位的方法列表
        print('支持的座位预定方式如下')
        time.sleep(0.7)
        print('='*12)
        print('+==========================+')
        print("1 - 指定行列号预定座位")
        print("2 - 给我预订一个最靠前的座位！")
        print('+==========================+')
        time.sleep(0.7)
        print('')

        # 获取座位预定方式
        method = input('请选择座位预定方式')
        # 定义合法的输入列表
        valid_method = ['1','2']
        # 当不符合要求时循环获取新的选项
        while method not in valid_method:
            method = input('没有按照要求输入哦，请重新输入')

        # 实例化SeatBooking类
        booking = SeatBooking()
        # 打印所有座位的预定信息
        booking.check_bookings(seats_list)
        # 方法一：指定行列号
        if method == '1':
            booking.book_seat(seats_list)
        else:
            booking.book_seat_at_front(seats_list)

        # 打印欢迎语
    def welcome(self):
        print('+============================+')
        print('+      欢迎来到时光电影院       +')
        print('+============================+')
        print('')
        time.sleep(0.7)

        # 打印结束语
    def bye(self):
        print('')
        time.sleep(0.7)
        print('+============================+')
        print('+    已经退出系统，下次见！👋    +')
        print('+============================+')

a = Controller(infos)




