import time
class FilmSelect:
    def display_options(self,films):
        print("今日影院排片列表：")
        print("="*12)
        for i in range(len(films)):
            print("{}-{}".format(i+1,films[i]['name']))
            time.sleep(0.2)
        # 打印退出选项
        print('x - 退出')
        print("="*12)
        time.sleep(0.7)

    def get_choice(self,films):
        # 符合要求的输入列表
        valid_choice = [str(i+1) for i in range(len(films))]
        valid_choice.append('x')

        choice = input("你的选择是？")
        # 当选择不满足要求的时候 循环重新获取新的选项
        while choice not in valid_choice:
            choice = input("你的选择是？")
        return choice



