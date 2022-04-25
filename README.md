# DataAnalyzeProject
## 此為大數據視覺化班一條龍專案,詳細內容如下 : 
- 主題 : 針對王品集團、瓦城泰統、漢來美食,進行餐飲趨勢分析,如:旗下各餐飲品牌聲量、消費者喜好轉換的趨勢等
- 資料源 : 愛食記、ptt food版、Google map評論、Tripadvisor、痞客邦
- 詳細步驟
1. 針對愛食記網頁爬取有用資訊,如:店家評分、按讚數、食記/評論內容...等,並將所爬取的資訊整理後存成CSV檔。    --愛食記資料蒐集.ipynb
   (google_map/PIXNET/Tripadvisor.csv來自別組貢獻)
2. 針對評論/食記內容進行情感分析,獲取分數作為一項參考值,並存成新的CSV檔。    --文本分析.ipynb
3. 利用python程式,一一將CSV檔讀取並匯入至mongoDB。    --CSV匯入mongo.ipynb
4. 架設API,供使用者存取其指定的集團餐廳的數據內容。    --API.py
5. Tableau直接連結mongoDB的資料,視覺化作圖以分析資料。    --MongoDB連上Tableau.txt
