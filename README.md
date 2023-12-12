## FoodTrendDataAnalyzeProject
### Trend analysis in the food industry for 3 companies in Taiwan, Wowprime, Viva Taiwan, and Han Lai Cuisine. This analysis includes factors such as brand popularity and consumer preference trends.
#### Data Sources: 
Data was collected from sources including iFoodie, PTT Food forum, Google Maps reviews, Tripadvisor, and Pixnet.
#### Detailed Steps: 
##### 1. Web scraping:
Web scraping from iFoodie to gather useful information such as restaurant ratings, likes, user reviews/comments, etc. The collected data is then organized and saved as CSV files.
##### 2. sentiment-analyzed 
The collected comments/reviews were sentiment-analyzed to get a score as a reference value, which was then saved as a new CSV file.
##### 3. Python -CSV -MongoDB 
Python scripts are used to read each CSV file and import them into MongoDB.
File: CSV to MongoDB.ipynb
##### 4. API for users queries
An API is created to allow users to access data related to their specified restaurant groups.
File: API.py
##### 5. Tableau visualization
Tableau connects to MongoDB data for data visualization and analysis.
File: Connecting MongoDB to Tableau.txt
#### Visualization links:
ifoodie: [Link](https://public.tableau.com/app/profile/fafa5465/viz/ifoodie/sheet8_1)

PTTFOOD: [Link](https://public.tableau.com/app/profile/fafa5465/viz/PTTFOOD/sheet2_1)

# DataAnalyzeProject
## 此為大數據視覺化班一條龍專案,詳細內容如下 : 
- 主題 : 針對王品集團、瓦城泰統、漢來美食,進行餐飲趨勢分析,如:旗下各餐飲品牌聲量、消費者喜好轉換的趨勢等
- 資料源 : 愛食記、ptt food版、Google map評論、Tripadvisor、痞客邦
- 甘特圖 : Task Schedule.html、資料庫欄位.html
- 詳細步驟
1. 爬取愛食記網頁有用資訊,如:店家評分、按讚數、食記/評論內容...等,並將所爬取的資訊整理後存成CSV檔。       
   --愛食記資料蒐集.ipynb  (google_map/PIXNET/Tripadvisor.csv CREDITED TO 其他組分享)
2. 針對評論/食記內容進行情感分析,獲取分數作為一項參考值,並存成新的CSV檔。    --文本分析.ipynb
3. 爬取PTT Food版    -- reviewNLP.py
4. 針對Ptt Food版,運用Jieba進行斷詞分析以獲得關鍵詞(消費者喜好分析)       -- Ptt Food Jieba.py
5. 利用python程式,一一將CSV檔讀取並匯入至mongoDB。    --CSV匯入mongo.ipynb
6. 架設API,供使用者存取其指定的集團餐廳的數據內容。    --API.py
7. Tableau直接連結mongoDB的資料,視覺化作圖以分析資料。    --MongoDB連上Tableau.txt
   - ifoodie視覺化連結 : https://public.tableau.com/app/profile/fafa5465/viz/ifoodie/sheet8_1
   - PTTFOOD連結 :https://public.tableau.com/app/profile/fafa5465/viz/PTTFOOD/sheet2_1
8. (加分)運用plotly作圖,直接在網頁上呈現內容    --cat_windrose.html、bubble.html、distribution.html
