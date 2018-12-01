
# coding: utf-8

# In[ ]:


#slurry_config.py

slurry_name = "slurry001"
topic_format = "slurry/{}/{}"
level_topic = topic_format.format(slurry_name, "level")
methane_topic = topic_format.format(slurry_name, "methane")

