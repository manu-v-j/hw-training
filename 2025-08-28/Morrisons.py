import csv
import pandas as pd

df=pd.read_csv("/home/toshiba/Hashwave/2025-08-28/dataset_reddit_morrisons.csv")
df['timestamp_utc'] = pd.to_datetime(df['timestamp'], unit='s', utc=True)

df['Post Date/Time'] = df['timestamp_utc'].dt.tz_convert('Asia/Kolkata')

df['Brand']='tesco'
df['brand_type']=''
df['Platform']='Morrisons'
df['Post ID/URL']="https://www.reddit.com" + df['permalink']
df['User Handle']=df['author']
df['Post Text/Caption']=df['title']
df['Engagement - Comments']=df['comments']
df['Image/Video URL']=df['image_url']
df['Engagement - Likes']=''
df['Engagement - Shares/Retweets']=''
df['Views (Video)']=''
df['Common Keywords']=''
df['Region']=''
df['Language']=''
df['Top Theme Tags']=''
df['Campaign Tag']=''
df['User Type']=''
df['Post Type']=''
df['Media Type']=''
df['Mentions Type']=''
df['Hashtags Used']=''
df = df.drop(columns=['author', 'timestamp', 'score','permalink','image_url','comments','title','author'])
df=df[['Brand','brand_type','Platform','Post ID/URL','Post Date/Time','User Handle','User Type','Post Text/Caption','Post Type','Media Type',
       'Mentions Type','Hashtags Used','Engagement - Likes','Engagement - Comments','Engagement - Shares/Retweets','Views (Video)','Common Keywords',
       'Region','Language','Top Theme Tags','Campaign Tag','Image/Video URL']]
df.to_csv("/home/toshiba/Hashwave/2025-08-28/reddit_morrisons.csv", index=False)
