from selenium import webdriver
import time
from PIL import Image
from numpy import average, dot, linalg
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
        # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
        image = image.resize(size, Image.ANTIALIAS)
        if greyscale:
            # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
            image = image.convert('L')
        return image

    # 计算图片的余弦距离
    def image_similarity_vectors_via_numpy(image1, image2):
        image1 = imgutl.get_thum(image1)
        image2 = imgutl.get_thum(image2)
        images = [image1, image2]
        vectors = []
        norms = []
        for image in images:
            vector = []
            for pixel_tuple in image.getdata():
                vector.append(average(pixel_tuple))
            vectors.append(vector)
            # linalg=linear（线性）+algebra（代数），norm则表示范数
            # 求图片的范数？？
            norms.append(linalg.norm(vector, 2))
        a, b = vectors
        a_norm, b_norm = norms
        # dot返回的是点积，对二维数组（矩阵）进行计算
        res = dot(a / a_norm, b / b_norm)
        return res

    def bijiao(self,img1,img2):
        image1 = Image.open(img1)
        image2 = Image.open(img2)
        cosin =imgutl.image_similarity_vectors_via_numpy(image1, image2)
        return cosin





