# -*- coding: utf-8 -*-
import yaml,json
import os,sys,shutil



json_path = 'config_raw.json'
#json原文件

json_path1 = 'config_raw.json'
#修改json文件后保存的路径

dict={}
#用来存储数据

def get_json_data(json_path):
#获取json里面数据

    with open(json_path,'rb') as f:
    #定义为只读模型，并定义名称为f
        a=open('account/account.txt')
        b=open('account/password.txt')
        line1 = a.readline().strip()
        line2 = b.readline().strip()
        params = json.load(f)
        #加载json文件中的内容给params
        
        params['account']['uin'] = line1
        params['account']['password'] = line2
        #修改内容
        
        print("params",params)
        #打印
        
        dict = params
        #将修改后的内容保存在dict中
        
    f.close()
    #关闭json读模式
    
    return dict
    #返回dict字典内容
def write_json_data(dict):
#写入json文件

    with open(json_path1,'w') as r:
    #定义为写模式，名称定义为r
    
        json.dump(dict,r)
        #将dict写入名称为r的文件中
        
    r.close()
    #关闭json写模式

the_revised_dict = get_json_data(json_path)
write_json_data(the_revised_dict)
#调用两个函数，更新内容

if __name__ =='__main__':
    with open('config_raw.json', encoding='utf-8') as f:
        line = f.readline()
        d = json.loads(line)
        dstr=json.dumps(d)   #dict转成字符
        dyaml=yaml.load(dstr)   #将字符转仓yaml
        filey = 'config.yml'
        stream = open(filey, 'w')
        yaml.safe_dump(dyaml, stream, default_flow_style=False)  #输出到文件中

# Read in the file contents as text
with open('config.yml') as f:
    invalid_json = f.read()

valid_json = invalid_json.replace("'", '')


# Save the modified text back to the file
with open('config.yml', 'w') as f:
    f.write(valid_json)

path = 'account'
for i in os.listdir(path):
   path_file = os.path.join(path,i)
   if os.path.isfile(path_file):
      os.remove(path_file)
   else:
     for f in os.listdir(path_file):
         path_file2 =os.path.join(path_file,f)
         if os.path.isfile(path_file2):
             os.remove(path_file2)

def open_app(app_dir1):
  os.startfile(app_dir1)
if __name__ == "__main__":
  app_dir1 = os.path.abspath("bot.py")
  open_app(app_dir1)



main = "go-cqhttp.exe"
r_v = os.system(main) 
print (r_v )
