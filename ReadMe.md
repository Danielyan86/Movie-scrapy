# 准备环境安装
- 测试环境 MacOS python3
- pip install scrapy 安装python 爬虫
- sudo brew install mongodb 安装MongoDB 
- 创建数据存储目录 sudo mkdir -p /data/db
- 启动mongoDB   sudo mongod


# 执行爬虫
- 此程序有两个爬虫，一个mtime是爬取电影名字，年代和连接放入本地mongoDB，另外一个是下载图片到本地文件夹
## 运行数据爬虫 
- scrapy crawl mtime 注意需要修改setting 中的ITEM_PIPELINES配置为movie.pipelines.MoviePipeline，
## 运行图片爬虫 
- scrapy crawl mPicture 
- 注意需要修改setting 中的ITEM_PIPELINES配置为 movie.pipelines.MyImagesPipeline，
- ITEM_PIPELINES中的IMAGES_STORE为图片文件保存路径
- IMAGES_MIN_HEIGHT和IMAGES_MIN_WIDTH为图片筛选参数,只有大于这个尺寸图片才会被保存在本地