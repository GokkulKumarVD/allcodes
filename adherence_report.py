# import numpy as np
# import snowflake.connector
# snowflake.connector.paramstyle = 'qmark'
import datetime
# from snowflake.sqlalchemy import URL
# from sqlalchemy import create_engine
import pandas as pd
import getpass

username = getpass.getuser()



# file_password = open('Password.txt')
#
# password = file_password.read()
# file_password.close()
# type(password)
# url = URL(
#     account='swiggy.ap-southeast-2',
#     user='vd.gokkulkumar@swiggy.in',
#     password=password,
#     database='FACTS',
#     schema='FIELD_CC_TEAM',
#     warehouse='NONTECH_WH_01',
#    authenticator='externalbrowser',
#     role='FIELD_CC_TEAM'
# )
#
# engine = create_engine(url)
# con = engine.connect()
#
# stmt = """select distinct
# a.order_id, to_date(ordered_time) order_date, ordered_time, foodissueid, issuedescl1, week(to_date(ordered_time)) week_number, resolvedby, agentid,
# case when pred = 0 then 'Non Fraud'
# when pred = 1 then 'Fraud' else 'No Prediction' end prediction,
# case when recommendationidshown is null then 'No Recommendation' else
# case when recommendationidshown[0] = 'NA' then 'Dont Give' else 'Give' end
# end recommendation_shown,
# case when ISRECOMMENDATIONFOLLOWED is null then
# case when recommendationidshown[0] = 'NA' then 'Yes' else 'No' end
# when ISRECOMMENDATIONFOLLOWED = 0 then 'No'
# when ISRECOMMENDATIONFOLLOWED = 1 then 'Yes'
# end recommendation_followed, resolutionsamount
# from
# facts.public.dp_order_fact a join (select distinct * from facts.public.igcc_fact) i
# on(a.order_id = i.orderid)
# left join
# (
#   Select * from (
# Select issue_id, order_id, prediction as pred
# ,row_number() over(partition by order_id, issue_id order by DT desc) as latest_pred
# from "STREAMS"."PUBLIC"."FRAUD_SEGMENT_DP_EVENT"
#   )
# where latest_pred =1)  p
# on i.orderid = p.order_id and i.FOODISSUEID = p.issue_id
#
# where
# ignore_order_flag = 0
# and to_date(ordered_time) = CURRENT_DATE - 1
# and a.post_status in ('Cancelled','Completed')"""
# try:
#     df = pd.read_sql(stmt, con)
#     con.execute(stmt)
#     igcc = pd.read_sql(stmt, con)
#     igcc.to_csv("C:\\Users\\"+ username +"\\Desktop\\projects\\IGCC_adherence_report\\data.csv")
# finally:
#     con.close()
#     engine.dispose()
#
# print('done')


df = pd.read_csv("C:\\Users\\"+ username +"\\Desktop\\projects\\IGCC_adherence_report\\data.csv")

df.fillna('NAN', inplace=True)

df.columns = map(lambda x: str(x).lower(), df.columns)


df['resolutionsamount'] = df['resolutionsamount'].replace('NAN',0)


df['agentid'] = df['agentid'].str.lower()

df['STATUS'] = ""

def osp(x):
    if "_cb" in x:
        return "CBSL"
    elif "_kt" in x:
        return "KOCHAR"
    elif "_tm" in x:
        return "TECH MAHINDRA"
    elif "_gr" in x:
        return "GRASS ROOTS"
    elif "_fs" in x:
        return "FIVE SPLASH"
    elif "_ag" in x:
        return "AEGIS"
    elif "ijp" in x:
        return "CENTRAL FOLLOW UP"
    elif "new.city" in x:
        return "NEW CITY"
    elif "_rm" in x:
        return "RADICAL MINDS"
    elif "_hrh" in x:
        return "HRH"
    elif "_ison" in x:
        return "ISON"
    elif "_g7cr" in x:
        return "G7"
    else:
        return "IN HOUSE"


df['STATUS'] = df['agentid'].apply(osp)

df['agentid'] = df['agentid'].str.split('@', expand=True)[0]


# dataframe


mp = pd.read_csv("C:\\Users\\"+username+"\\Desktop\\projects\\IGCC_adherence_report\\manpower.csv")
mp['agentid'] = mp['agentid'].str.lower()

df = pd.merge(df,mp,how='left',on='agentid')

date = df.iat[1,1]


df.to_csv("C:\\Users\\"+username+"\\Desktop\\projects\\IGCC_adherence_report\\Validated_IGCC_data"+ date +".csv",index=False)
df['lob'].fillna('Others',inplace=True)

df_full = df

df_omt_igcc = df[(df['lob']=='IGCC') | (df['lob']=='OMT') ].shape[0]

df = df[(df['recommendation_shown']!='No Recommendation') & (df['lob']!='IGCC') & (df['lob']!='OMT') ]

# created multiple dataframe for fraud and non fraud
df_fraud = df[df['prediction'] == 'Fraud']
df_not_fraud = df[df['prediction'] == 'Non Fraud']

df_fraud_count = df_fraud.shape[0]
df_not_fraud_count = df_not_fraud.shape[0]


# igcc issue created total
df_full_tot_count = df_full.shape[0]

df_omt_igcc = df_omt_igcc / df_full_tot_count

fraud_customer_contribution_total = df_fraud_count / df_full_tot_count
non_fraud_customer_contribution_total = df_not_fraud_count / df_full_tot_count

# no recommendation count
df_norecommendation_count = df_full[df_full['recommendation_shown'] == 'No Recommendation'].shape[0]

# igcc issues created , no recommendation total
total_norecommendation_percentage = df_norecommendation_count / df_full_tot_count

# recommendation available total
recommendation_available_total_percentage = 1 - total_norecommendation_percentage - df_omt_igcc

# excluded no recommendation
df_exclude_no_recommendation = df[~(df['recommendation_shown'] == 'No Recommendation')]



# non fraud customer contribution / recommendation give and dont give
df_not_fraud_give_count = df_not_fraud[df_not_fraud['recommendation_shown'] == 'Give'].shape[0]
df_not_fraud_dont_give_count = df_not_fraud[df_not_fraud['recommendation_shown'] == 'Dont Give'].shape[0]


issues_created_non_fraud_give_percentage = df_not_fraud_give_count / df_full_tot_count
issues_created_non_fraud_dont_give_percentage = df_not_fraud_dont_give_count / df_full_tot_count


# next part starts here -----------------------------

# fraud_customer_total_percentage
second_df_fraud_customer_total_percentage =  df_fraud[(df_fraud['resolvedby'] == 'Agent') | (df_fraud['resolvedby'] == 'Bot')].shape[0] / df_fraud.shape[0]
second_df_fraud_customer_total_percentage =1-second_df_fraud_customer_total_percentage

# second_non_fraud_customer_total
second_not_fraud_customer_total_percentage = df_not_fraud[df_not_fraud['recommendation_followed'] == 'Yes'].shape[0] / df_not_fraud.shape[0]

# recommendation available total
# adherence_recommendation_available_total_percentage = 1 - second_df_fraud_customer_total_percentage

adherence_recommendation_available_total_percentage = ((second_df_fraud_customer_total_percentage*fraud_customer_contribution_total)+(second_not_fraud_customer_total_percentage*non_fraud_customer_contribution_total))/(fraud_customer_contribution_total+non_fraud_customer_contribution_total)





# second give
second_adhernce_give_percentage = df_not_fraud[ (df_not_fraud['recommendation_followed'] == 'Yes') & (df_not_fraud['recommendation_shown'] == 'Give')].shape[0] / df_not_fraud[df_not_fraud['recommendation_shown'] == 'Give'].shape[0]

# second_dont_give
second_adhernce_dont_give_percentage = df_not_fraud[ (df_not_fraud['recommendation_followed'] == 'Yes') & (df_not_fraud['recommendation_shown'] == 'Dont Give')].shape[0] / df_not_fraud[df_not_fraud['recommendation_shown'] == 'Dont Give'].shape[0]

# # run another query to get counts of order id
# file_password = open('Password.txt')
# password = file_password.read()
# file_password.close()
# type(password)
# url = URL(
#     account='swiggy.ap-southeast-1',
#     user='vd.gokkulkumar@swiggy.in',
#     password=password,
#     database='FACTS',
#     schema='FIELD_CC_TEAM',
#     warehouse='NONTECH_WH_01',
#    authenticator='externalbrowser',
#     role='FIELD_CC_TEAM'
# )
#
# engine = create_engine(url)
# con = engine.connect()
#
# stmt = "select Count(order_id) from facts.public.dp_order_fact a where a.dt= current_date -1 and ignore_order_flag=0 and post_status in ('Completed')"
#
# try:
#     df = pd.read_sql(stmt, con)
#     con.execute(stmt)
#     igcc = pd.read_sql(stmt, con)
#     igcc.to_csv("C:\\Users\\"+username+"\\Desktop\\projects\\IGCC_adherence_report\\order_id_count.csv",index=False)
# finally:
#     con.close()
#     engine.dispose()
#
# print('done')
#
#
#
#
# # reading total count of order id
# cnt = pd.read_csv("C:\\Users\\"+username+"\\Desktop\\projects\\IGCC_adherence_report\\order_id_count.csv")
# cnt = cnt.iat[0,0]

cnt = 603053


# igcc_cpo
igcc_cpo_sum = df_full['resolutionsamount'].sum()
igcc_cpo_total = round(igcc_cpo_sum / cnt,2)

df_full_igcc_omt = df_full[(df_full['lob'] == 'IGCC') | (df_full['lob'] == 'OMT')]
df_full_igcc_omt_amount = df_full_igcc_omt['resolutionsamount'].sum()
df_full_igcc_omt_amount = round(df_full_igcc_omt_amount / cnt,2)

df_fraud_igcc_cpo_total = df_fraud['resolutionsamount'].sum()
df_fraud_igcc_cpo_total = round(df_fraud_igcc_cpo_total / cnt,2)

df_not_fraud_adh_total = df_not_fraud['resolutionsamount'].sum()
df_not_fraud_total = round(df_not_fraud_adh_total / cnt,2)


# igcc cpo non fraud customer

# df_not_fraud_igcc_cpo_total = df_not_fraud['resolutionsamount'].sum()
# df_not_fraud_igcc_cpo_total = df_not_fraud_igcc_cpo_total / cnt

df_not_fraud_adh_igcc_cpo_total = df_not_fraud[df_not_fraud['recommendation_followed'] == 'Yes']
df_not_fraud_adh_igcc_cpo_total = df_not_fraud_adh_igcc_cpo_total['resolutionsamount'].sum()
df_not_fraud_adh_igcc_cpo_total = round(df_not_fraud_adh_igcc_cpo_total / cnt,2)


df_not_fraud_non_adh_igcc_cpo_total = df_not_fraud[df_not_fraud['recommendation_followed'] == 'No']
df_not_fraud_adh_total = df_not_fraud_non_adh_igcc_cpo_total['resolutionsamount'].sum()
df_not_nonadh_fraud_total = round(df_not_fraud_adh_total / cnt,2)



# LOB wise data

df_full_non_adherence_cases = df_full[(df_full['resolvedby'] == 'Agent') & (df_full['recommendation_shown'] != 'No Recommendation')]

df_full_non_adherence_fraud = df_full_non_adherence_cases[(df_full_non_adherence_cases['prediction']=='Fraud') & (df_full_non_adherence_cases['resolvedby'] != 'NAN')]

df_full_non_adherence_fraud_cases_total = df_full_non_adherence_fraud['order_id'].shape[0]


# /////////////////////

df_full_non_adherence_nonfraud_cases = df_full[(df_full['resolvedby'] == 'Agent') & (df_full['recommendation_shown'] != 'No Recommendation') & (df_full['recommendation_followed'] == 'No')]

df_full_non_adherence_nonfraud = df_full_non_adherence_nonfraud_cases[(df_full_non_adherence_nonfraud_cases['prediction']=='Non Fraud') & (df_full_non_adherence_nonfraud_cases['resolvedby'] != 'NAN') & (df_full_non_adherence_nonfraud_cases['recommendation_followed'] == 'No')]

df_full_non_adherence_nonfraud_cases_total = df_full_non_adherence_nonfraud['order_id'].shape[0]


# ///////

df_full_non_adherence_cases_total = df_full_non_adherence_fraud_cases_total + df_full_non_adherence_nonfraud_cases_total

df_full_non_adherence_cases_fraud_total = df_full_non_adherence_fraud_cases_total / df_full_non_adherence_cases_total
# chat
df_full_non_adherence_fraud_chat_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'CC'].shape[0]
df_full_non_adherence_fraud_chat = df_full_non_adherence_fraud_chat_total / df_full_non_adherence_cases_total


# voice
df_full_non_adherence_fraud_voice_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'Voice'].shape[0]
df_full_non_adherence_fraud_voice = df_full_non_adherence_fraud_voice_total / df_full_non_adherence_cases_total


# email
df_full_non_adherence_fraud_email_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'Email'].shape[0]
df_full_non_adherence_fraud_email = df_full_non_adherence_fraud_email_total / df_full_non_adherence_cases_total



# social media
df_full_non_adherence_fraud_sm_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'SM'].shape[0]
df_full_non_adherence_fraud_sm = df_full_non_adherence_fraud_sm_total / df_full_non_adherence_cases_total


# OMT
df_full_non_adherence_fraud_omt_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'OMT'].shape[0]
df_full_non_adherence_fraud_omt = df_full_non_adherence_fraud_omt_total / df_full_non_adherence_cases_total


# ED
df_full_non_adherence_fraud_ed_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'ED'].shape[0]
df_full_non_adherence_fraud_ed = df_full_non_adherence_fraud_ed_total / df_full_non_adherence_cases_total



# swat
df_full_non_adherence_fraud_swat_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'Swat'].shape[0]
df_full_non_adherence_fraud_swat = df_full_non_adherence_fraud_swat_total / df_full_non_adherence_cases_total



# ps
df_full_non_adherence_fraud_ps_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'PS'].shape[0]
df_full_non_adherence_fraud_ps = df_full_non_adherence_fraud_ps_total / df_full_non_adherence_cases_total



# igcc
df_full_non_adherence_fraud_igcc_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'IGCC'].shape[0]
df_full_non_adherence_fraud_igcc = df_full_non_adherence_fraud_igcc_total / df_full_non_adherence_cases_total


# others
df_full_non_adherence_fraud_others_total = df_full_non_adherence_fraud[df_full_non_adherence_fraud['lob']== 'Others'].shape[0]
df_full_non_adherence_fraud_others = df_full_non_adherence_fraud_others_total / df_full_non_adherence_cases_total



# non fraud--------------------------------------------------------------------------------------------



df_full_non_adherence_cases_nonfraud_total = df_full_non_adherence_nonfraud_cases_total / df_full_non_adherence_cases_total

# chat
df_full_non_adherence_nonfraud_chat_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'CC'].shape[0]
df_full_non_adherence_nonfraud_chat = df_full_non_adherence_nonfraud_chat_total / df_full_non_adherence_cases_total


# voice
df_full_non_adherence_nonfraud_voice_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'Voice'].shape[0]
df_full_non_adherence_nonfraud_voice = df_full_non_adherence_nonfraud_voice_total / df_full_non_adherence_cases_total


# email
df_full_non_adherence_nonfraud_email_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'Email'].shape[0]
df_full_non_adherence_nonfraud_email = df_full_non_adherence_nonfraud_email_total / df_full_non_adherence_cases_total


# sm
df_full_non_adherence_nonfraud_sm_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'SM'].shape[0]
df_full_non_adherence_nonfraud_sm = df_full_non_adherence_nonfraud_sm_total / df_full_non_adherence_cases_total


# omt
df_full_non_adherence_nonfraud_omt_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'OMT'].shape[0]
df_full_non_adherence_nonfraud_omt = df_full_non_adherence_nonfraud_omt_total / df_full_non_adherence_cases_total



# ed
df_full_non_adherence_nonfraud_ed_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'ED'].shape[0]
df_full_non_adherence_nonfraud_ed = df_full_non_adherence_nonfraud_ed_total / df_full_non_adherence_cases_total


# swat
df_full_non_adherence_nonfraud_swat_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'Swat'].shape[0]
df_full_non_adherence_nonfraud_swat = df_full_non_adherence_nonfraud_swat_total / df_full_non_adherence_cases_total


# igcc
df_full_non_adherence_nonfraud_igcc_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'IGCC'].shape[0]
df_full_non_adherence_nonfraud_igcc = df_full_non_adherence_nonfraud_igcc_total / df_full_non_adherence_cases_total




# others
df_full_non_adherence_nonfraud_others_total = df_full_non_adherence_nonfraud[df_full_non_adherence_nonfraud['lob']== 'Others'].shape[0]
df_full_non_adherence_nonfraud_others = df_full_non_adherence_nonfraud_others_total / df_full_non_adherence_cases_total



# here = pd.concat([df_aht_frt_aegis, df_aht_frt_kochar, df_aht_frt_tm, df_aht_frt_cbsl, df_aht_frt_ison, df_aht_frt_inhouse], axis=1)
here = pd.DataFrame({'A': df_full_tot_count, 'B': df_omt_igcc, 'C':recommendation_available_total_percentage, 'D':fraud_customer_contribution_total, 'E':non_fraud_customer_contribution_total, 'F':issues_created_non_fraud_give_percentage, 'G':issues_created_non_fraud_dont_give_percentage, 'H':total_norecommendation_percentage, 'I':adherence_recommendation_available_total_percentage, 'J':second_df_fraud_customer_total_percentage, 'K':second_not_fraud_customer_total_percentage, 'L':second_adhernce_give_percentage, 'M':second_adhernce_dont_give_percentage, 'N':igcc_cpo_total, 'O':df_full_igcc_omt_amount, 'P':df_fraud_igcc_cpo_total, 'Q':df_not_fraud_total, 'R':df_not_fraud_adh_igcc_cpo_total, 'S':df_not_nonadh_fraud_total, 'T':df_full_non_adherence_cases_total, 'U':df_full_non_adherence_cases_fraud_total, 'V':df_full_non_adherence_fraud_chat, 'W':df_full_non_adherence_fraud_voice, 'X':df_full_non_adherence_fraud_email, 'Y':df_full_non_adherence_fraud_sm, 'Z':df_full_non_adherence_fraud_omt, 'aa':df_full_non_adherence_fraud_ed, 'ab':df_full_non_adherence_fraud_swat, 'ac':df_full_non_adherence_fraud_ps, 'ad':df_full_non_adherence_fraud_igcc, 'ae':df_full_non_adherence_fraud_others, 'af':df_full_non_adherence_cases_nonfraud_total, 'ag':df_full_non_adherence_nonfraud_chat, 'ah':df_full_non_adherence_nonfraud_voice, 'ai':df_full_non_adherence_nonfraud_email, 'aj':df_full_non_adherence_nonfraud_sm, 'ak':df_full_non_adherence_nonfraud_omt, 'al':df_full_non_adherence_nonfraud_ed, 'am':df_full_non_adherence_nonfraud_swat, 'an':df_full_non_adherence_nonfraud_igcc, 'ao':df_full_non_adherence_nonfraud_others}, index=[0])



here.to_csv("C:\\Users\\"+username+"\\Desktop\\projects\\IGCC_adherence_report\\current_date_1.csv",index=False)