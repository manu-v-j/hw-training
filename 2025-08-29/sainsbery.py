import json,os
import pandas as pd
with open("/home/toshiba/Hashwave/2025-08-29/dataset_facebook_sainsbury.json", "r") as f:
    data = json.load(f)
    for item in data:
        url=item.get('url','')
        text=item.get('text','')
        time=item.get('time','')
        likes=item.get('likes','')
        comments=item.get('comments','')
        shares=item.get('shares','')
        media_list=item.get('media',[])
        for media in media_list:
            image_url=''

            if "photo_image" in media:
                image_url=media.get("photo_image", {}).get("uri", "")

            elif "image" in media:
                image_url=media.get("image", {}).get("uri", "")

        item = {}
        item['Brand'] = 'sainsburys'
        item['brand_type'] = ''
        item['Platform'] = 'facebook'
        item['Post ID/URL'] = url
        item['Post Date/Time'] = time
        item['User Handle'] = ''
        item['User Type'] = ''
        item['Post Text/Caption'] = text
        item['Post Type'] = ''
        item['Media Type'] = ''
        item['Mentions Type'] = ''
        item['Hashtags Used'] = ''
        item['Engagement - Likes'] = likes
        item['Engagement - Comments'] = comments
        item['Engagement - Shares/Retweets'] = shares
        item['Views (Video)'] = ''
        item['Common Keywords'] = ''
        item['Region'] = ''
        item['Language'] = ''
        item['Top Theme Tags'] = ''
        item['Campaign Tag'] = ''
        item['Image/Video URL'] = image_url

        df = pd.DataFrame([item])
        headers=['Brand','brand_type','Platform','Post ID/URL','Post Date/Time','User Handle','User Type','Post Text/Caption','Post Type',
                 'Media Type','Mentions Type','Hashtags Used','Engagement - Likes','Engagement - Comments','Engagement - Shares/Retweets',
                 'Views (Video)','Common Keywords','Region','Language','Top Theme Tags','Campaign Tag','Image/Video URL']
        
        filename = "sainsbury.csv"

        if not os.path.isfile(filename):
            df.to_csv(filename, mode="w", header=headers, index=False, encoding="utf-8-sig")
        else:
            df.to_csv(filename, mode="a", header=False, index=False, encoding="utf-8-sig")