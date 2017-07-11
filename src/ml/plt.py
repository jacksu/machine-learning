
# coding: utf-8

# In[1]:


import pandas as pd
tweets = pd.read_csv("tweets.csv")
tweets.head()


# In[3]:


def get_candidate(row):
        candidates = []
        text = row["text"].lower()
        if "clinton" in text or "hillary" in text:
            candidates.append("clinton")
        if "trump" in text or "donald" in text:
            candidates.append("trump")
        if "sanders" in text or "bernie" in text:
            candidates.append("sanders")
        return ",".join(candidates)
    
tweets["candidate"] = tweets.apply(get_candidate,axis=1)
tweets.head()


# In[14]:


import matplotlib.pyplot as plt
import numpy as np
counts = tweets["candidate"].value_counts()
plt.bar(range(len(counts)), counts)
plt.show()


# In[16]:


#用户年龄统计
from datetime import datetime
    
tweets["created"] = pd.to_datetime(tweets["created"])
tweets["user_created"] = pd.to_datetime(tweets["user_created"])
    
tweets["user_age"] = tweets["user_created"].apply(lambda x: (datetime.now() - x).total_seconds() / 3600 / 24 / 365)
plt.hist(tweets["user_age"])
plt.title("Tweets mentioning candidates")
plt.xlabel("Twitter account age in years")
plt.ylabel("# of tweets")
plt.show()


# In[23]:


cl_tweets = tweets["user_age"][tweets["candidate"] == "clinton"]
sa_tweets = tweets["user_age"][tweets["candidate"] == "sanders"]
tr_tweets = tweets["user_age"][tweets["candidate"] == "trump"]
plt.hist([
        cl_tweets, 
        sa_tweets, 
        tr_tweets
        ],
    stacked=True, 
    label=["clinton", "sanders", "trump"]
)
plt.legend()
plt.title("Tweets mentioning each candidate")
plt.xlabel("Twitter account age in years")
plt.ylabel("# of tweets")
plt.annotate('More Trump tweets', xy=(2, 35000), xytext=(3, 35000),
                arrowprops=dict(facecolor='black'))
plt.show()


# In[24]:


import matplotlib.colors as colors
    
tweets["red"] = tweets["user_bg_color"].apply(lambda x: colors.hex2color('#{0}'.format(x))[0])
tweets["blue"] = tweets["user_bg_color"].apply(lambda x: colors.hex2color('#{0}'.format(x))[2])
fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flat
    
ax0.hist(tweets["red"])
ax0.set_title('Red in backgrounds')
    
ax1.hist(tweets["red"][tweets["candidate"] == "trump"].values)
ax1.set_title('Red in Trump tweeters')
    
ax2.hist(tweets["blue"])
ax2.set_title('Blue in backgrounds')
    
ax3.hist(tweets["blue"][tweets["candidate"] == "trump"].values)
ax3.set_title('Blue in Trump tweeters')
    
plt.tight_layout()
plt.show()


# In[26]:


gr = tweets.groupby("candidate").agg([np.mean, np.std])
    
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(7, 7))
ax0, ax1 = axes.flat
    
std = gr["polarity"]["std"].iloc[1:]
mean = gr["polarity"]["mean"].iloc[1:]
ax0.bar(range(len(std)), std)
ax0.set_xticklabels(std.index, rotation=30)
ax0.set_title('Standard deviation of tweet sentiment')
    
ax1.bar(range(len(mean)), mean)
ax1.set_xticklabels(mean.index, rotation=45)
ax1.set_title('Mean tweet sentiment')
    
plt.tight_layout()
plt.show()
