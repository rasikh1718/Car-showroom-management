
from django.db import models


import pymysql
import datetime
import os


# Create your models here.

def get_file_path(request,filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename= "%s %s"%(nowtime,original_filename)
    return os.path.join('upload/',filename)

class Company(models.Model):
    slug= models.CharField(max_length=150,null=False, blank=False)
    name= models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=get_file_path, null=True, blank=True)
    nowheel=models.IntegerField(default=0, null=False, blank=False)
    engine=models.CharField(max_length=150,null=False ,blank=False)
    cartype=models.CharField(max_length=150,null=False ,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    slug= models.CharField(max_length=150,null=False, blank=False)
    name= models.CharField(max_length=150,null=False, blank=False)
    company=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path, null=True, blank=True)
    nowheel=models.IntegerField(default=0, null=False, blank=False)
    engine=models.CharField(max_length=150,null=False ,blank=False)
    fuel=models.CharField(max_length=150,null=False ,blank=False)
    cartype=models.CharField(max_length=150,null=False ,blank=False)
    price=models.FloatField(default=0 ,null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class cartypesearch:
#     def cartype(self,type):
#         context={}
#         con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',passwd='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')
#         curs=con.cursor()
#         curs.execute("select * from Product where cartype=%s"%type)
#         data=curs.fetchall()
#         print(data)
#         # if data:
#         #     dic={"list":data}
#         # else:
#         #     dic['name']='Not found'            
#         if data:
#             context['name']=data[2]
#             context['cartype']=data[8]
#         else:
#             context['name']='not found'
#             context['cartype']='not found'
#         con.close()
#         return context