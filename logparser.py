#!/usr/bin/env python3

#############################MODULES################################
import sys

############################FUNTIONS################################

#########################################
###function for log parsing##############
#########################################
## " and 'id=' are the line separaters ##

def apache_output(line):
    myid = line.split('"')
    myid = myid[3].split('id=')
    myid = myid[1].split()
    myid = myid[0]

    ip = line.split()
    ip = ip[3]

    uagent = line.split('"')

    return myid, ip, uagent ;

#########################################
###function for log filtration###########
#########################################
##  filtering the log with 'gif' word  ## 

def gif_finder(file):
    for line in file:
        if 'gif' in line:
             yield line



############################MAIN LOGICS###########################################

if __name__ == "__main__":

    try:
        log_name1 = sys.argv[1]
        log_name2 = sys.argv[2]

        log1 = open(log_name1, 'r')
        log2 = open(log_name2, 'r')

    except IndexError:
        print ("You must specify the files to parse. Two files is needed by the script")
        sys.exit(1)

    log1 = gif_finder(log1)
    log2 = gif_finder(log2)

    list1=[]
    list_id1=[]
    for line in log1:
        line_id1, ip, uagent = apache_output(line)
        list_id1.append(line_id1)
        uagent = uagent[35]
        list_full1 = (line_id1, ip, uagent)
        list1.append(list_full1)

    list2=[]
    for line in log2:
        line_id2, ip, uagent = apache_output(line)
        list2.append(line_id2)
    
    matched = set(list_id1) & set(list2)
    print("LOG1 & LOG2 MATCHED ID's COUNT:", len(matched))
    unique_id_in_1 = set(list_id1).difference(list2)
    print("LOG1 ONLY ID's COUNT:          ", len(unique_id_in_1))

    for item1 in unique_id_in_1: 
        for item2 in list1:
            if item1 == item2[0]:
                print("LOG1 ID's INFO:                ", item2)


    log1.close()
    log2.close()

