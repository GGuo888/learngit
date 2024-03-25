import time

class SeatBooking:
    #展示所有座位的信息
    def check_bookings(self,seats):
        print("正在为您查询该场次电影的预定状态...")
        time.sleep(0.7)
        print("从上到下为1~6排，从左到右为1~8座")
        print("="*12)
        for row in seats:
            time.sleep(0.1)
            print('  '.join(row))
        print("="*12)
        time.sleep(0.7)

    # 获取符合要求的行索引
    def get_row(self):
        input_row = input("预定第几排的座位呢？请输入1~6之间的数字")
        valid_row = [str(i+1) for i in range(6)]

        while input_row not in valid_row:
            input_row = input('没有按要求输入哦，请重新输入1~6之间的数字')

        row = int(input_row) - 1
        return row
    # 获取符合要求的列索引
    def get_col(self):
        input_column = input('预定这一排的第几座呢？请输入1~8之间的数字')
        valid_column = [str(i+1) for i in range(8)]

        while input_column not in valid_column:
            input_column = input('没有按要求输入哦，请输入1~8之间的数字')

        column = int(input_column)-1
        return column
    # 预定指定的座位
    def book_seat(self,seats):
        while True:
            row = self.get_row()
            col = self.get_col()

            if seats[row][col] == '○':
                print("正在为您预定座位...")
                time.sleep(0.7)
                seats[row][col] == '●'
                print("预定成功！座位号：{}排{}座".format(row+1,col+1))
                break
            else:
                print("这个座位已经被预定了哦，试试别的吧")
                time.sleep(0.7)


    # 预定最靠前的座位
    def book_seat_at_front(self,seats):
        print("正在为您预定最靠前的座位")
        time.sleep(0.7)
        for row in range(6):# 外层循环遍历seats的行
            for col in range(8):# 内层循环遍历seats的列
                if seats[row][col] == '○':
                    seats[row][col] = '●'
                    print("预定成功！座位号:{}排{}座".format(row+1,col+1))
                    return
        print("非常抱歉所有座位都被预定满了，无法为您保留座位")






