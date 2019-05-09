######################################
# setup variable for the application  
v_print_ver = 1
v_print_conf = 1
v_print_debug_msg = 1 
v_print_data_analysis = 1
# End setup variable for the application 
#########################################

#########################################
# Print config 
if v_print_conf == 1:
        print("\nVariable configuration parameters ")
        print('v_print_ver: {}' .format(v_print_ver))
        print('v_print_conf: {}' .format(v_print_conf))
        print('v_print_debug_msg: {}' .format(v_print_debug_msg))
        
#END Print config 
######################################
        
# Load libraries
try:
    if v_print_debug_msg == 1 :
        print('Msg: Import libraries')
    import sys
    import numpy as np    
    import matplotlib as plt
    import cv2
    import pandas as pd
except ImportError:
    print('Error: Failed to load mudules')

# end import libraries 
#########################################
    
#########################################
#Print versions
if v_print_ver == 1 :
    print("\nVersions of all librries used in this application ")
    print('Python: {}'.format(sys.version))
    print('numpy: {}' .format(np.__version__))
    print('cv2: {}'.format(cv2.__version__))
    print('matplotlib: {}'.format(plt.__version__))
    print('Pandas: {}'.format(pd.__version__))
#end print versions
#########################################
    
    
movies_df = pd.read_csv('IMDB-Movie-Data.csv' ,index_col="Title")

print(movies_df.head(5))
print(movies_df.info())


temp_df = movies_df.append(movies_df)
print(movies_df.shape)
print(temp_df.shape)

temp_df.drop_duplicates(inplace=True , keep='first')
print(temp_df.shape)
print(movies_df.columns)

movies_df.rename(columns={'Runtime (Minutes)':'Runtime' , 'Revenue (Millions)': 'Revenue' }, inplace=True)
print(movies_df.columns)
print(movies_df.isnull().sum())


revenue = movies_df['Revenue']
print(revenue.head(10))

prom = movies_df.loc[["Prometheus" , "Sing"]]
print(prom)


condition = movies_df[movies_df['Director'] == "Ridley Scott"]


#condition = movies_df[(movies_df['Director'] == "Ridley Scott")|(movies_df['Director'] == "Christopher Nolan")]
condition = movies_df[movies_df['Director'].isin( ["Ridley Scott" , "Christopher Nolan"])]
print(condition)












