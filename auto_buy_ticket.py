from splinter.browser import Browser
from time import sleep
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

class Buy_Tickets(object):
    def __init__(self,orders,passengers,starts,ends,dtime):
        # 车次，0代表所有车次，依次从上到下，1代表列表显示第一班车次，依次类推
        self.orders = orders
        #乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.initMy_url = "https://kyfw.12306.cn/otn/view/index.html"
        self.ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.driver_name = "chrome"
        
        
    #查询功能
    def check(self,order):
        try:
            self.driver.find_by_text('预定')[ order -1 ].click()
            sleep(1.5)
        except Exception as e:
            print(e)
            print("预定失败")

    # 买票功能
    def start_buy(self):
        self.pool = ThreadPool()
        self.driver = Browser(driver_name=self.driver_name)
        self.driver.driver.maximize_window()
        #登录
        self.driver.visit(self.login_url)
        sleep(1)
        while True:
            if self.driver.url != self.initMy_url:
                sleep(1)
            else:
                break
        self.driver.visit(self.ticket_url)
        try:
            print("开始购票...")
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation":self.starts})
            self.driver.cookies.add({"_jc_save_toStation":self.ends})
            self.driver.cookies.add({"_jc_save_fromDate":self.dtime})
            self.driver.reload()
            count = 0
            if self.orders != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text("查询").click()
                    count += 1
                    print("第%d次点击查询" % count)
                    start = datetime.now()
                    self.pool.map(self.check,self.orders)
                    end = datetime.now()
                    print((end - start).total_seconds())
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text("查询").click()
                    count += 1
                    print("第%次点击查询" % count)
                    try:
                        for i in self.driver.find_by_text('预定'):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print("预定失败")
                        continue
            print('开始预定')
            sleep(1)
            print("开始选择用户")
            for p in self.passengers:
                self.driver.find_by_text(p).last.click()
                sleep(1)
                if p[-1] == ')':
                    self.driver.find_by_id('dialog_xsertcj_ok').click()
            print('提交订单')
            self.driver.find_by_id("submitOrder_id").click()
            sleep(2)
            print("确认选座")
            self.driver.find_by_id("qr_submit_id").click()
            print('预定成功')
            self.pool.close()
            self.pool.join()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    orders = [2,3,4]
    # 乘客名，比如passengers = ['XXX', 'XXX']
    # 学生票需注明，注明方式为：passengers = ['XXX(学生)', 'XXX']
    passengers = ['张峻']
    dtime = '2022-06-03'
    #出发地、目的地(需填写cookie值)
    starts = '%u6210%u90FD%2CCDW'
    ends = '%u7EF5%u9633%2CMYW'

    Buy_Tickets(orders,passengers,starts,ends,dtime).start_buy()


