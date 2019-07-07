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
    import pandas as pd
    import os
    import time
    from datetime import datetime 
    
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
    print('matplotlib: {}'.format(plt.__version__))
    print('Pandas: {}'.format(pd.__version__))
#end print versions
#########################################
    
    
path  = "C:/Users/werne/Documents/GitHub/Python/Practice/StockData/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date' , 'Unix' , 'Ticker' , 'DE Ratio', 'Price' ,'SP500' ])
    
    #sp500 = pd.DataFrame.from_csv('YAHOO-INDEX_GSPC.csv')
    sp500_df = pd.read_csv('YAHOO-INDEX_GSPC.csv')

    
    #print(stock_list)
    for each_dir in stock_list[1:25]:
        each_file  = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        if len(each_file) >0  :
            for file in each_file:
                date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                #print(date_stamp)
                full_file_path = each_dir + '/'+file
                source = open(full_file_path,'r').read()
                #print(source)
                
                #print(ticker+":"+value)
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value  = float(row["Adjusted Close"])
                    except:
                        if v_print_debug_msg == 1 :
                            print('EXCEPTION: Failed to assign adjusted values')
                        sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])
                        
                    
                    df = df.append({'Date':date_stamp , 'Unix':unix_time , 'Ticker':ticker , 'DE Ratio':value} , ignore_index =True)
                except Exception as e:
                    pass
    #print(gather)           
    save = gather.replace(' ' , '').replace('(','').replace('/' ,'').replace(')' ,'')+'.csv'
    #print(save)
    df.to_csv(save)
            
            
            
Key_Stats()
