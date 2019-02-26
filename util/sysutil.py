from selenium import webdriver
import time
from PIL import Image
#from numpy import average, dot, linalg
import operator

class httputil():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.option = webdriver.FirefoxOptions()

    def login(self,url,name,pas):
        self.httpcurl =url
        self.driver.get(self.httpcurl)
        time.sleep(5)
        self.driver.get_screenshot_as_file("/home/h/"+self.driver.title+".png")
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(name)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pas)
        time.sleep(5)
        self.driver.find_element_by_id('login-submit').click()
        time.sleep(5)
        #for link in self.driver.find_elements_by_xpath("//*[@ul]"):  # 获取当前页面的href
        #    lis = link.find_elements_by_xpath('li')
          #  print (lis)
        #namelink = namelinks.get_attribute("placeholder")
        #print(namelink)
        #tcurl = "http://123.127.164.20:21935/#!ADC_project_staff_html"
        #self.driver.get(tcurl)
        print("lkkk")
        return


    def bytag(self,url,tag1,tag2):
        self.driver.get(url)
        time.sleep(2)
        uls = self.driver.find_elements_by_tag_name(tag1)
        for link in uls:  # 获取当前页面的href
            lis = link.find_elements_by_tag_name(tag2)
        return (lis)

    def bytag_att(self,url,att1):
        self.driver.get(url)
        time.sleep(2)
        uls = self.driver.find_elements_by_tag_name(att1)
        return (uls)

class imgutl():



    # 对图片进行统一化处理
    def get_thum(image, size=(64, 64), greyscale=False):

        return image

    # 计算图片的余弦距离
    def image_similarity_vectors_via_numpy(image1, image2):

        return

    def bijiao(self,img1,img2):

        return





