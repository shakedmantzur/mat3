# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:18:46 2021

@author: Shaked
"""


def whatsapp():
    file=open("WhatsAppT.txt", encoding='utf8')
    dic_id=dict()
    dic_p=dict()
    dic2=dict()
    list_dic=list()
    date_time=0
    num_id=0
    for line in file:
        line=line.strip()
        if not':' in line:
            dic_p['datetime']=date_time
            dic_p['id']=num_id
            dic_p['text']=line
            list_dic.append(dic_p.copy())
            continue
        indexA=line.find('-')+1
        indexB=line.find(':',indexA)
        if indexB>0:
            name=line[indexA:indexB]
            if name not in dic_id:
                num_id=num_id+1
                dic_id[name]=num_id
                time=line[0:15]
                date_time1=time.replace(',','')
                dic_p['datetime']=date_time1
                dic_p['id']=num_id
                text=line.split(':')
                dic_p['text']=text[2]
                date_time=date_time1
                list_dic.append(dic_p.copy())
            else:
                time=line[0:15]
                date_time1=time.replace(',','')
                dic_p['datetime']=date_time1
                dic_p['id']=dic_id[name]
                text=line.split(':')
                dic_p['text']=text[2]
                date_time=date_time1
                list_dic.append(dic_p.copy())
    #print(list_dic)
    file2=open("WhatsAppT.txt", encoding='utf8')
    for line2 in file2:
        line2=line2.strip()
        if 'נוצרה על ידי' in line2:
            index1=line2.find('"')
            index2=line2.find('"',index1)
            if index2>0:
                c_name=line2.split('"')
                cn= c_name[1]
                dic2['chat_name']=cn
                c=line2.split('ידי')
                dic2['creation_date']=line2[0:15]
                dic2['num_of_participants']=num_id
                dic2['creator']=c[1]
                
           
    #print(dic2)
    dic_p_2=dict()
    dic_p_2['messages']=list_dic
    dic_p_2['metadata']=dic2
    print(dic_p_2)
    import json
    json_f=cn+".txt"
    with open(json_f, 'w', encoding='utf8') as json_f:
        json.dump(dic_p_2,json_f, ensure_ascii=False)
    
    
   
G=whatsapp()   
