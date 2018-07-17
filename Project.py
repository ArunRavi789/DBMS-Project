from tkinter import *
from sqlite3 import *
from tkinter import messagebox

root=Tk()
root.title("CRICKET FANTASY XI")

conn = connect('cricket.sqlite')
cur=conn.cursor()
cur1=conn.cursor()

name=StringVar()
ID_bat=StringVar()
ID_ball=StringVar()
ID_field=StringVar()
ID_bat_coach=StringVar()
ID_ball_coach=StringVar()
ID_field_coach=StringVar()
COACH_ID=StringVar()
ID_play=StringVar()

unique_const=0

first = 0
last = 1

bats_count=0
balls_count=0
field_count=0
coach_count=0
player_count=0

sel_all_bat=0
sel_run=0
sel_avg_bat=0
sel_mat_bat=0
sel_hs=0
sel_100=0

sel_all_ball=0
sel_wic=0
sel_avg_ball=0
sel_mat_ball=0
sel_bp=0
sel_5wh=0

sel_all_field=0
sel_cat=0
sel_mc=0
sel_mat_field=0
sel_cpr=0

bat_count_coach=0
ball_count_coach=0
field_count_coach=0

sel_bat_coach_all=0
sel_bat_coach_count=0
sel_bat_coach_hpw=0
sel_bat_coach_iq=0

sel_ball_coach_all=0
sel_ball_coach_count=0
sel_ball_coach_hpw=0
sel_ball_coach_iq=0

sel_field_coach_all=0
sel_field_coach_count=0
sel_field_coach_hpw=0
sel_field_coach_iq=0


frame1=Frame(root)
frame5=Frame(root)
frame6=Frame(root)
frame7=Frame(root)

def create_tables():
    cur.execute('Drop table Team')
    cur.execute('Drop table Coach')
    cur.execute('CREATE TABLE Team (player_id TEXT PRIMARY KEY,name TEXT,code INTEGER)')
    cur.execute('CREATE TABLE Coach (coach_id TEXT PRIMARY KEY,name TEXT,code INTEGER)')

def login():
    
    def start():
        
        root.geometry("800x100")

        def batsmen():     
            def add_player():                
                global bats_count
                global player_count
                global unique_const
                unique_const=0
                if(bats_count>=8):
                    messagebox.showinfo("MESSAGE","Max Batsman Added")
                    cb1.deselect()
                    cb2.deselect()
                    cb3.deselect()
                    cb4.deselect()
                    cb5.deselect()
                    cb6.deselect()
                    
                    global sel_all_bat
                    global sel_run
                    global sel_avg_bat
                    global sel_mat_bat
                    global sel_100
                    global sel_hs

                    sel_all_bat=0
                    sel_run=0
                    sel_avg_bat=0
                    sel_mat_bat=0
                    sel_100=0
                    sel_hs=0

                    frame5.destroy()
                    frame6.destroy()
                    frame7.destroy()

                    start()

                else:
                    num=ID_bat.get()
                    cur.execute('Select Player_id from Team')
                    for row in cur:
                        if(num==row[0]):
                            unique_const=1
                            
                    cur.execute('Select * from Batsmen where Player_id=?',(num,))
                    for row in cur:
                        if(unique_const==0):
                            cur1.execute('Insert into Team values(?,?,0)',(row[0],row[1],))
                            messagebox.showinfo("MESSAGE","Batsman Added")
                            bats_count=bats_count+1
                            player_count=player_count+1
                        else:
                            messagebox.showinfo("MESSAGE","Player Already Added")
                    

            def back():
                cb1.deselect()
                cb2.deselect()
                cb3.deselect()
                cb4.deselect()
                cb5.deselect()
                cb6.deselect()

                global sel_all_bat
                global sel_run
                global sel_avg_bat
                global sel_mat_bat
                global sel_100
                global sel_hs

                sel_all_bat=0
                sel_run=0
                sel_avg_bat=0
                sel_mat_bat=0
                sel_100=0
                sel_hs=0

                frame5.destroy()
                frame6.destroy()
                frame7.destroy()

                start() 
            
            def all_flg():
                global sel_all_bat
                if(sel_all_bat==1):
                    sel_all_bat=0
                else:
                    sel_all_bat=1
            def run_flg():
                global sel_run
                if(sel_run==1):
                    sel_run=0
                else:
                    sel_run=1
            def avg_flg():
                global sel_avg_bat
                if(sel_avg_bat==1):
                    sel_avg_bat=0
                else:
                    sel_avg_bat=1
            def mat_flg():
                global sel_mat_bat
                if(sel_mat_bat==1):
                    sel_mat_bat=0
                else:
                    sel_mat_bat=1
            def hun_flg():
                global sel_100
                if(sel_100==1):
                    sel_100=0
                else:
                    sel_100=1
            def hs_flg():
                global sel_hs
                if(sel_hs==1):
                    sel_hs=0
                else:
                    sel_hs=1

            def search():
                global first
                global last    
                if(sel_all_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                #5C5
                elif(sel_run==1 and sel_avg_bat==1 and sel_mat_bat==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Batting_average>45 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                #5C4
                elif(sel_run==1 and sel_avg_bat==1 and sel_mat_bat==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Batting_average>45 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_avg_bat==1 and sel_mat_bat==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Batting_average>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_mat_bat==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_avg_bat==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Batting_average>45 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_mat_bat==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Batting_average>45 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                #5C3
                elif(sel_run==1 and sel_mat_bat==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_avg_bat==1 and sel_mat_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Batting_average>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_mat_bat==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_avg_bat==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Batting_average>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_avg_bat==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Batting_average>45 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_bat==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_mat_bat==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Batting_average>45 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_mat_bat==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Batting_average>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Batting_average>45 and Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                #5C2
                elif(sel_run==1 and sel_mat_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Matches>350')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_avg_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Batting_average>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_run==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_bat==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_mat_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Batting_average>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_bat==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Batting_average>45 and Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Batting_average>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_100==1 and sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Hundreds>45 and Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                #5C1
                elif(sel_run==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Runs>18000')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Batting_average>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_bat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Matches>350')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_100==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Hundreds>45')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                elif(sel_hs==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM Batsmen WHERE Highest_score>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Runs         Average             Hundreds     HS                Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[6])+"                    "+str(row[1]))
                    last=i
                else:
                    mylist.delete(first,last)
                    first=0
                    mylist.insert(0,"NULL")
                    last=0
                    
            root.geometry("1000x600")

            frame5=Frame(root)
            frame6=Frame(root)
            frame7=Frame(root)
            frameb=Frame(root)

            frame3.destroy()
            frame4.destroy()

            frame5.place(x=0,y=0,height=600,width=400)
            frame6.place(x=400,y=0,height=500,width=600)
            frame7.place(x=500,y=500,height=50,width=400)
            frameb.place(x=500,y=550,height=50,width=400)

            cb1=Checkbutton(frame5,text="Select All",onvalue=1,offvalue=0,height=5,width=20,command=all_flg)
            cb2=Checkbutton(frame5,text="Runs>18000",onvalue=1,offvalue=0,height=5,width=20,command=run_flg)
            cb3=Checkbutton(frame5,text="Average>45",onvalue=1,offvalue=0,height=5,width=20,command=avg_flg)
            cb4=Checkbutton(frame5,text="Matches>350",onvalue=1,offvalue=0,height=5,width=20,command=mat_flg)
            cb5=Checkbutton(frame5,text="Hundreds>45",onvalue=1,offvalue=0,height=5,width=20,command=hun_flg)
            cb6=Checkbutton(frame5,text="Highest Score>200",onvalue=1,offvalue=0,height=5,width=20,command=hs_flg)
            go=Button(frame5,text="search",command=search)
            cb1.pack()
            cb2.pack()
            cb3.pack()
            cb4.pack()
            cb5.pack()
            cb6.pack()
            go.pack()

            scroll=Scrollbar(frame6)
            scroll.pack(side=RIGHT,fill=Y)

            mylist=Listbox(frame6,height=400,width=400,yscrollcommand=scroll.set)
            scroll.config(command=mylist.yview)
            mylist.pack(side=LEFT,fill=BOTH)

            user=Label(frame7,text="Player Id:")
            user.pack(side=LEFT)
            insert=Entry(frame7,textvariable=ID_bat)
            insert.pack(side=RIGHT)
            add=Button(frameb,text="ADD",command=add_player)
            add.pack(side=LEFT)
            back=Button(frameb,text="BACK",command=back)
            back.pack(side=RIGHT)
            
        def bowlers():
            def add_player():
                global balls_count
                global unique_const
                global player_count
                unique_const=0
                if(balls_count>=6):
                    messagebox.showinfo("MESSAGE","Max Bowlers Added")
                    global sel_all_ball
                    global sel_wic
                    global sel_avg_ball
                    global sel_mat_ball
                    global sel_bp
                    global sel_5wh

                    sel_all_ball=0
                    sel_wic=0
                    sel_avg_ball=0
                    sel_mat_ball=0
                    sel_bp=0
                    sel_5wh=0

                    cb7.deselect()
                    cb8.deselect()
                    cb9.deselect()
                    cb10.deselect()
                    cb11.deselect()
                    cb12.deselect()

                    frame8.destroy()
                    frame9.destroy()
                    frame10.destroy()

                    start()
                else:
                    num=ID_ball.get()
                    cur.execute('Select Player_id from Team')
                    for row in cur:
                        if(num==row[0]):
                            unique_const=1
                            
                    cur.execute('Select * from bowlers where Player_id=?',(num,))
                    for row in cur:
                        if(unique_const==0):
                            cur1.execute('Insert into Team values(?,?,1)',(row[0],row[1],))
                            messagebox.showinfo("MESSAGE","Bowler Added")
                            balls_count=balls_count+1
                            player_count=player_count+1
                        else:
                            messagebox.showinfo("MESSAGE","Player Already Added")

            def back():
                global sel_all_ball
                global sel_wic
                global sel_avg_ball
                global sel_mat_ball
                global sel_bp
                global sel_5wh

                sel_all_ball=0
                sel_wic=0
                sel_avg_ball=0
                sel_mat_ball=0
                sel_bp=0
                sel_5wh=0

                cb7.deselect()
                cb8.deselect()
                cb9.deselect()
                cb10.deselect()
                cb11.deselect()
                cb12.deselect()

                frame8.destroy()
                frame9.destroy()
                frame10.destroy()

                start()

            def all_flg():
                global sel_all_ball
                if(sel_all_ball==1):
                    sel_all_ball=0
                else:
                    sel_all_ball=1
            def wic_flg():
                global sel_wic
                if(sel_wic==1):
                    sel_wic=0
                else:
                    sel_wic=1
            def avg_flg():
                global sel_avg_ball
                if(sel_avg_ball==1):
                    sel_avg_ball=0
                else:
                    sel_avg_ball=1
            def mat_flg():
                global sel_mat_ball
                if(sel_mat_ball==1):
                    sel_mat_ball=0
                else:
                    sel_mat_ball=1
            def bp_flg():
                global sel_bp
                if(sel_bp==1):
                    sel_bp=0
                else:
                    sel_bp=1
            def wh_flg():
                global sel_5wh
                if(sel_5wh==1):
                    sel_5wh=0
                else:
                    sel_5wh=1

            def search():
                global first
                global last 
                if(sel_all_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                #5C5
                elif(sel_wic==1 and sel_avg_ball==1 and sel_mat_ball==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Bowling_average<30 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                #5C4
                elif(sel_wic==1 and sel_avg_ball==1 and sel_mat_ball==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Bowling_average<30 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_avg_ball==1 and sel_mat_ball==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Bowling_average<30 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_mat_ball==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_avg_ball==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Bowling_average<30 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_mat_ball==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Bowling_average<30 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                #5C3
                elif(sel_wic==1 and sel_mat_ball==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_avg_ball==1 and sel_mat_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Bowling_average<30')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_mat_ball==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_avg_ball==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Bowling_average<30 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_avg_ball==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Bowling_average<30 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_ball==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_mat_ball==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Bowling_average<30 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_mat_ball==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Bowling_average<30 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Bowling_average<30 and Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                #5C2
                elif(sel_wic==1 and sel_mat_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Matches>150')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_avg_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Bowling_average<30')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_wic==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_ball==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_mat_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Bowling_average<30')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_ball==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Bowling_average<30 and Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Bowling_average<30 and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_bp==1 and sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Best_performance Like "8%" and Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                #5C1
                elif(sel_wic==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Wickets>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_avg_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Bowling_average<30')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_mat_ball==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Matches>150')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_bp==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Best_performance Like "8%"')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                elif(sel_5wh==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM bowlers WHERE Five_wicket_hauls>5')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Wickets      Average        BP          5WH                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"      "+str(row[3])+"          "+str(row[4])+"                "+str(row[6])+"           "+str(row[5])+"                    "+str(row[1]))
                    last=i
                else:
                    mylist.delete(first,last)
                    first=0
                    mylist.insert(0,"NULL")
                    last=0

            
            frame3.destroy()
            frame4.destroy()
            
            root.geometry("1000x600")

            frame8=Frame(root)
            frame9=Frame(root)
            frame10=Frame(root)
            frameb=Frame(root)

            frame8.place(x=0,y=0,height=600,width=400)
            frame9.place(x=400,y=0,height=500,width=600)
            frame10.place(x=500,y=500,height=50,width=400)
            frameb.place(x=500,y=550,height=50,width=400)

            cb7=Checkbutton(frame8,text="Select All",onvalue=1,offvalue=0,height=5,width=20,command=all_flg)
            cb8=Checkbutton(frame8,text="Wickets>200",onvalue=1,offvalue=0,height=5,width=20,command=wic_flg)
            cb9=Checkbutton(frame8,text="Average<30",onvalue=1,offvalue=0,height=5,width=20,command=avg_flg)
            cb10=Checkbutton(frame8,text="Matches>150",onvalue=1,offvalue=0,height=5,width=20,command=mat_flg)
            cb11=Checkbutton(frame8,text="Best Performance = 8 wickets",onvalue=1,offvalue=0,height=5,width=20,command=bp_flg)
            cb12=Checkbutton(frame8,text="5 Wicket Hauls>5",onvalue=1,offvalue=0,height=5,width=20,command=wh_flg)
            go=Button(frame8,text="search",command=search)
            cb7.pack()
            cb8.pack()
            cb9.pack()
            cb10.pack()
            cb11.pack()
            cb12.pack()
            go.pack()

            scroll=Scrollbar(frame9)
            scroll.pack(side=RIGHT,fill=Y)

            mylist=Listbox(frame9,height=400,width=400,yscrollcommand=scroll.set)
            scroll.config(command=mylist.yview)
            mylist.pack(side=LEFT,fill=BOTH)

            user=Label(frame10,text="Player Id:")
            user.pack(side=LEFT)
            insert=Entry(frame10,textvariable=ID_ball)
            insert.pack(side=RIGHT)
            add=Button(frameb,text="ADD",command=add_player)
            add.pack(side=LEFT)
            back=Button(frameb,text="BACK",command=back)
            back.pack(side=RIGHT)
            
        def fielders():
            def add_player():
                global field_count
                global unique_const
                global player_count
                unique_const=0
                if(field_count>=2):
                    messagebox.showinfo("MESSAGE","Max Fielders Added")
                    global sel_all_field
                    global sel_cat
                    global sel_mc
                    global sel_mat_field
                    global sel_cpr

                    sel_all_field=0
                    sel_cat=0
                    sel_mc=0
                    sel_mat_field=0
                    sel_cpr=0

                    cb13.deselect()
                    cb14.deselect()
                    cb15.deselect()
                    cb16.deselect()
                    cb17.deselect()

                    frame11.destroy()
                    frame12.destroy()
                    frame13.destroy()

                    start()

                else:
                    num=ID_field.get()
                    cur.execute('Select Player_id from Team')
                    for row in cur:
                        if(num==row[0]):
                            unique_const=1
                            
                    cur.execute('Select * from fielders where Player_id=?',(num,))
                    for row in cur:
                        if(unique_const==0):
                            cur1.execute('Insert into Team values(?,?,2)',(row[0],row[1],))
                            messagebox.showinfo("MESSAGE","Fielder Added")
                            field_count=field_count+1
                            player_count=player_count+1
                        else:
                            messagebox.showinfo("MESSAGE","Player Already Added")

            def back():
                global sel_all_field
                global sel_cat
                global sel_mc
                global sel_mat_field
                global sel_cpr

                sel_all_field=0
                sel_cat=0
                sel_mc=0
                sel_mat_field=0
                sel_cpr=0

                cb13.deselect()
                cb14.deselect()
                cb15.deselect()
                cb16.deselect()
                cb17.deselect()

                frame11.destroy()
                frame12.destroy()
                frame13.destroy()

                start()

            def all_flg():
                global sel_all_field
                if(sel_all_field==1):
                    sel_all_field=0
                else:
                    sel_all_field=1
            def cat_flg():
                global sel_cat
                if(sel_cat==1):
                    sel_cat=0
                else:
                    sel_cat=1
            def mc_flg():
                global sel_mc
                if(sel_mc==1):
                    sel_mc=0
                else:
                    sel_mc=1
            def mat_flg():
                global sel_mat_field
                if(sel_mat_field==1):
                    sel_mat_field=0
                else:
                    sel_mat_field=1
            def cpr_flg():
                global sel_cpr
                if(sel_cpr==1):
                    sel_cpr=0
                else:
                    sel_cpr=1

            def search():
                global first
                global last 
                if(sel_all_field==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                #4C4
                elif(sel_cat==1 and sel_mat_field==1 and sel_cpr==1 and sel_mc==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Matches>200 and Max_catches>3 and Catches_per_innings>0.35')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                #4C3
                elif(sel_cat==1 and sel_mc==1 and sel_mat_field==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Matches>200 and Max_catches>3')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_cat==1 and sel_mat_field==1 and sel_cpr==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Matches>200 and Catches_per_innings>0.35')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_cat==1 and sel_mc==1 and sel_cpr==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Max_catches>3 and Catches_per_innings>0.35')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_mc==1 and sel_mat_field==1 and sel_cpr==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Matches>200 and Max_catches>3 and Catches_per_innings>0.35')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                #4C2
                elif(sel_cat==1 and sel_mat_field==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Matches>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_cat==1 and sel_mc==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Max_catches>3')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_cat==1 and  sel_cpr==1  ):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100 and Catches_per_innings>0.35  ')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_mat_field==1 and  sel_cpr==1  ):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Matches>200 and Catches_per_innings>0.35  ')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_mc==1 and sel_mat_field==1  ):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Matches>200 and Max_catches>3  ')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")  
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_mc==1 and  sel_cpr==1  ):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Max_catches>3 and Catches_per_innings>0.35  ')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                #4C1
                elif(sel_cat==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches>100')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_mc==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Max_catches>3')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_mat_field==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Matches>200')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                elif(sel_cpr==1):
                    mylist.delete(first,last)
                    first=0
                    cur.execute('SELECT * FROM fielders WHERE Catches_per_innings>0.35')
                    i=1
                    mylist.insert(0,"PLAYER ID     Matches     Catches      MC            CPI                   Name")
                    for row in cur:
                        i=i+1
                        mylist.insert(i,str(row[0])+"              "+str(row[2])+"          "+"         "+str(row[3])+"          "+str(row[4])+"                "+str(row[5])+"           "+str(row[1]))
                    last=i
                else:
                    mylist.delete(first,last)
                    first=0
                    mylist.insert(0,"NULL")
                    last=0

                    
            root.geometry("1000x600")

            frame11=Frame(root)
            frame12=Frame(root)
            frame13=Frame(root)
            frameb=Frame(root)

            frame3.destroy()
            frame4.destroy()

            frame11.place(x=0,y=0,height=600,width=400)
            frame12.place(x=400,y=0,height=500,width=600)
            frame13.place(x=500,y=500,height=50,width=400)
            frameb.place(x=500,y=550,height=50,width=400)

            cb13=Checkbutton(frame11,text="Select All",onvalue=1,offvalue=0,height=5,width=20,command=all_flg)
            cb14=Checkbutton(frame11,text="Catches>100",onvalue=1,offvalue=0,height=5,width=20,command=cat_flg)
            cb15=Checkbutton(frame11,text="Max Catches>3",onvalue=1,offvalue=0,height=5,width=20,command=mc_flg)
            cb16=Checkbutton(frame11,text="Matches>200",onvalue=1,offvalue=0,height=5,width=20,command=mat_flg)
            cb17=Checkbutton(frame11,text="Catches Per Innings>0.35",onvalue=1,offvalue=0,height=5,width=20,command=cpr_flg)
            go=Button(frame11,text="search",command=search)
            cb13.pack()
            cb14.pack()
            cb15.pack()
            cb16.pack()
            cb17.pack()
            go.pack()

            scroll=Scrollbar(frame12)
            scroll.pack(side=RIGHT,fill=Y)

            mylist=Listbox(frame12,height=400,width=400,yscrollcommand=scroll.set)
            scroll.config(command=mylist.yview)
            mylist.pack(side=LEFT,fill=BOTH)

            user=Label(frame13,text="Player Id:")
            user.pack(side=LEFT)
            insert=Entry(frame13,textvariable=ID_field)
            insert.pack(side=RIGHT)
            add=Button(frameb,text="ADD",command=add_player)
            add.pack(side=LEFT)
            back=Button(frameb,text="BACK",command=back)
            back.pack(side=RIGHT)

        def coaches():
            def bat_coach():
                def add_coach():
                    global bat_count_coach
                    global coach_count
                    global unique_const
                    unique_const=0
                    if(bat_count_coach>=1):
                        messagebox.showinfo("MESSAGE","Max Batting Coach Added")
                        cb19.deselect()
                        cb20.deselect()
                        cb21.deselect()
                        cb22.deselect()

                        global sel_bat_coach_all
                        global sel_bat_coach_count
                        global sel_bat_coach_hpw
                        global sel_bat_coach_iq
            
                        sel_bat_coach_all=0
                        sel_bat_coach_count=0
                        sel_bat_coach_hpw=0
                        sel_bat_coach_iq=0

                        frame19.destroy()
                        frame20.destroy()
                        frame21.destroy()

                        coaches()
                    else:
                        num=ID_bat_coach.get()
                        cur.execute('Select Coach_id from Coach')
                        for row in cur:
                            if(num==row[0]):
                                unique_const=1
                            
                        cur.execute('Select * from Batting_coach where Coach_id=?',(num,))
                        for row in cur:
                            if(unique_const==0):
                                cur1.execute('Insert into Coach values(?,?,0)',(row[0],row[1],))
                                messagebox.showinfo("MESSAGE","Batting Coach Added")
                                bat_count_coach=bat_count_coach+1
                                coach_count=coach_count+1
                            else:
                                messagebox.showinfo("MESSAGE","Coach Already Added")

                def back():
                    cb19.deselect()
                    cb20.deselect()
                    cb21.deselect()
                    cb22.deselect()

                    global sel_bat_coach_all
                    global sel_bat_coach_count
                    global sel_bat_coach_hpw
                    global sel_bat_coach_iq
        
                    sel_bat_coach_all=0
                    sel_bat_coach_count=0
                    sel_bat_coach_hpw=0
                    sel_bat_coach_iq=0

                    frame19.destroy()
                    frame20.destroy()
                    frame21.destroy()

                    coaches()

                def sel_all():
                    global sel_bat_coach_all
                    if(sel_bat_coach_all==0):
                        sel_bat_coach_all=1
                    else:
                        sel_bat_coach_all=0

                def sel_country():
                    global sel_bat_coach_count
                    if(sel_bat_coach_count==0):
                        sel_bat_coach_count=1
                    else:
                        sel_bat_coach_count=0

                def sel_hpw():
                    global sel_bat_coach_hpw
                    if(sel_bat_coach_hpw==0):
                        sel_bat_coach_hpw=1
                    else:
                        sel_bat_coach_hpw=0

                def sel_iq():
                    global sel_bat_coach_iq
                    if(sel_bat_coach_iq==0):
                        sel_bat_coach_iq=1
                    else:
                        sel_bat_coach_iq=0

                def search():
                    global first
                    global last    
                    if(sel_bat_coach_all==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_iq==1 and sel_bat_coach_hpw==1 and sel_bat_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Improvement_Quotient>6 and Hours_per_week>16 and Country="Australia"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i                                 
                    elif(sel_bat_coach_iq==1 and sel_bat_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Improvement_Quotient>6 and Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_iq==1 and sel_bat_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Improvement_Quotient>6 and Country="Australia"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_hpw==1 and sel_bat_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Country="Australia" and Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_iq==1 and sel_bat_coach_count==1 and sel_bat_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Country="Australia" and Hours_per_week>16 and Improvement_Quotient>6')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_iq==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Improvement_Quotient>6')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_bat_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Batting_coach WHERE Country="Australia"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    else:
                        mylist.delete(first,last)
                        first=0
                        mylist.insert(0,"NULL")
                        last=0
                    
                       
                root.geometry("1000x600")

                frame19=Frame(root)
                frame20=Frame(root)
                frame21=Frame(root)
                frameb=Frame(root)

                frame14.destroy()
                frame15.destroy()

                frame19.place(x=0,y=0,height=600,width=400)
                frame20.place(x=400,y=0,height=500,width=600)
                frame21.place(x=500,y=500,height=50,width=400)
                frameb.place(x=500,y=550,height=50,width=400)

                cb19=Checkbutton(frame19,text="Select All",onvalue=1,offvalue=0,height=5,width=20,command=sel_all)
                cb20=Checkbutton(frame19,text="Country='Australia'",onvalue=1,offvalue=0,height=5,width=20,command=sel_country)
                cb21=Checkbutton(frame19,text="Hours Per Week>16",onvalue=1,offvalue=0,height=5,width=20,command=sel_hpw)
                cb22=Checkbutton(frame19,text="Improvement Qutient>6",onvalue=1,offvalue=0,height=5,width=20,command=sel_iq)
                go=Button(frame19,text="search",command=search)
                cb19.pack()
                cb20.pack()
                cb21.pack()
                cb22.pack()
                go.pack()

                scroll=Scrollbar(frame20)
                scroll.pack(side=RIGHT,fill=Y)

                mylist=Listbox(frame20,height=400,width=400,yscrollcommand=scroll.set)
                scroll.config(command=mylist.yview)
                mylist.pack(side=LEFT,fill=BOTH)

                user=Label(frame21,text="Coach Id:")
                user.pack(side=LEFT)
                insert=Entry(frame21,textvariable=ID_bat_coach)
                insert.pack(side=RIGHT)
                add=Button(frameb,text="ADD",command=add_coach)
                add.pack(side=LEFT)
                back=Button(frameb,text="BACK",command=back)
                back.pack(side=RIGHT)

            def ball_coach():
                def add_coach():
                    global ball_count_coach
                    global coach_count
                    global unique_const
                    unique_const=0
                    if(ball_count_coach>=1):
                        messagebox.showinfo("MESSAGE","Max Bowling Coach Added")
                        cb25.deselect()
                        cb26.deselect()
                        cb27.deselect()
                        cb28.deselect()

                        global sel_ball_coach_all
                        global sel_ball_coach_count
                        global sel_ball_coach_hpw
                        global sel_ball_coach_iq
            
                        sel_ball_coach_all=0
                        sel_ball_coach_count=0
                        sel_ball_coach_hpw=0
                        sel_ball_coach_iq=0

                        frame22.destroy()
                        frame23.destroy()
                        frame24.destroy()

                        coaches()
                    else:
                        num=ID_ball_coach.get()
                        cur.execute('Select Coach_id from Coach')
                        for row in cur:
                            if(num==row[0]):
                                unique_const=1
                            
                        cur.execute('Select * from Bowling_coach where Coach_id=?',(num,))
                        for row in cur:
                            if(unique_const==0):
                                cur1.execute('Insert into Coach values(?,?,1)',(row[0],row[1],))
                                messagebox.showinfo("MESSAGE","Bowling Coach Added")
                                ball_count_coach=ball_count_coach+1
                                coach_count=coach_count+1
                            else:
                                messagebox.showinfo("MESSAGE","Coach Already Added")

                def back():
                    cb25.deselect()
                    cb26.deselect()
                    cb27.deselect()
                    cb28.deselect()

                    global sel_ball_coach_all
                    global sel_ball_coach_count
                    global sel_ball_coach_hpw
                    global sel_ball_coach_iq
            
                    sel_ball_coach_all=0
                    sel_ball_coach_count=0
                    sel_ball_coach_hpw=0
                    sel_ball_coach_iq=0

                    frame22.destroy()
                    frame23.destroy()
                    frame24.destroy()

                    coaches()

                def sel_all():
                    global sel_ball_coach_all
                    if(sel_ball_coach_all==0):
                        sel_ball_coach_all=1
                    else:
                        sel_ball_coach_all=0

                def sel_country():
                    global sel_ball_coach_count
                    if(sel_ball_coach_count==0):
                        sel_ball_coach_count=1
                    else:
                        sel_ball_coach_count=0

                def sel_hpw():
                    global sel_ball_coach_hpw
                    if(sel_ball_coach_hpw==0):
                        sel_ball_coach_hpw=1
                    else:
                        sel_ball_coach_hpw=0

                def sel_iq():
                    global sel_ball_coach_iq
                    if(sel_ball_coach_iq==0):
                        sel_ball_coach_iq=1
                    else:
                        sel_ball_coach_iq=0

                def search():
                    global first
                    global last    
                    if(sel_ball_coach_all==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_iq==1 and sel_ball_coach_hpw==1 and sel_ball_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Improvement_Quotient>6 and Hours_per_week>16 and Country="Australia"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i                                 
                    elif(sel_ball_coach_iq==1 and sel_ball_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Improvement_Quotient>6 and Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_iq==1 and sel_ball_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Improvement_Quotient>6 and Country="Australia"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_hpw==1 and sel_ball_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Country="Australia" and Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_iq==1 and sel_ball_coach_count==1 and sel_ball_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Country="Australia" and Hours_per_week>16 and Improvement_Quotient>6')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_iq==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Improvement_Quotient>6')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_ball_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Bowling_coach WHERE Country="Australia"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    else:
                        mylist.delete(first,last)
                        first=0
                        mylist.insert(0,"NULL")
                        last=0
                           
                root.geometry("1000x600")

                frame22=Frame(root)
                frame23=Frame(root)
                frame24=Frame(root)
                frameb=Frame(root)
                
                frame14.destroy()
                frame15.destroy()

                frame22.place(x=0,y=0,height=600,width=400)
                frame23.place(x=400,y=0,height=500,width=600)
                frame24.place(x=500,y=500,height=50,width=400)
                frameb.place(x=500,y=550,height=50,width=400)

                cb25=Checkbutton(frame22,text="Select All",onvalue=1,offvalue=0,height=5,width=20,command=sel_all)
                cb26=Checkbutton(frame22,text="Country='Australia'",onvalue=1,offvalue=0,height=5,width=20,command=sel_country)
                cb27=Checkbutton(frame22,text="Hours Per Week>16",onvalue=1,offvalue=0,height=5,width=20,command=sel_hpw)
                cb28=Checkbutton(frame22,text="Improvement Qutient>6",onvalue=1,offvalue=0,height=5,width=20,command=sel_iq)
                go=Button(frame22,text="search",command=search)
                cb25.pack()
                cb26.pack()
                cb27.pack()
                cb28.pack()
                go.pack()

                scroll=Scrollbar(frame23)
                scroll.pack(side=RIGHT,fill=Y)

                mylist=Listbox(frame23,height=400,width=400,yscrollcommand=scroll.set)
                scroll.config(command=mylist.yview)
                mylist.pack(side=LEFT,fill=BOTH)

                user=Label(frame24,text="Coach Id:")
                user.pack(side=LEFT)
                insert=Entry(frame24,textvariable=ID_ball_coach)
                insert.pack(side=RIGHT)
                add=Button(frameb,text="ADD",command=add_coach)
                add.pack(side=LEFT)
                back=Button(frameb,text="BACK",command=back)
                back.pack(side=RIGHT)

            def field_coach():
                def add_coach():
                    global field_count_coach
                    global coach_count
                    global unique_const
                    unique_const=0
                    if(field_count_coach>=1):
                        messagebox.showinfo("MESSAGE","Max Fielding Coach Added")
                        cb31.deselect()
                        cb32.deselect()
                        cb33.deselect()
                        cb34.deselect()

                        global sel_field_coach_all
                        global sel_field_coach_count
                        global sel_field_coach_hpw
                        global sel_field_coach_iq
            
                        sel_field_coach_all=0
                        sel_field_coach_count=0
                        sel_field_coach_hpw=0
                        sel_field_coach_iq=0

                        frame25.destroy()
                        frame26.destroy()
                        frame27.destroy()

                        coaches()
                    else:
                        num=ID_field_coach.get()
                        cur.execute('Select Coach_id from Coach')
                        for row in cur:
                            if(num==row[0]):
                                unique_const=1
                            
                        cur.execute('Select * from Fielding_coach where Coach_id=?',(num,))
                        for row in cur:
                            if(unique_const==0):
                                cur1.execute('Insert into Coach values(?,?,2)',(row[0],row[1],))
                                messagebox.showinfo("MESSAGE","Fielding Coach Added")
                                field_count_coach=field_count_coach+1
                                coach_count=coach_count+1
                            else:
                                messagebox.showinfo("MESSAGE","Coach Already Added")

                def back():
                    cb31.deselect()
                    cb32.deselect()
                    cb33.deselect()
                    cb34.deselect()

                    global sel_field_coach_all
                    global sel_field_coach_count
                    global sel_field_coach_hpw
                    global sel_field_coach_iq
            
                    sel_field_coach_all=0
                    sel_field_coach_count=0
                    sel_field_coach_hpw=0
                    sel_field_coach_iq=0

                    frame25.destroy()
                    frame26.destroy()
                    frame27.destroy()

                    coaches()


                def sel_all():
                    global sel_field_coach_all
                    if(sel_field_coach_all==0):
                        sel_field_coach_all=1
                    else:
                        sel_field_coach_all=0

                def sel_country():
                    global sel_field_coach_count
                    if(sel_field_coach_count==0):
                        sel_field_coach_count=1
                    else:
                        sel_field_coach_count=0

                def sel_hpw():
                    global sel_field_coach_hpw
                    if(sel_field_coach_hpw==0):
                        sel_field_coach_hpw=1
                    else:
                        sel_field_coach_hpw=0

                def sel_iq():
                    global sel_field_coach_iq
                    if(sel_field_coach_iq==0):
                        sel_field_coach_iq=1
                    else:
                        sel_field_coach_iq=0

                def search():
                    global first
                    global last    
                    if(sel_field_coach_all==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_iq==1 and sel_field_coach_hpw==1 and sel_field_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Improvement_Quotient>6 and Hours_per_week>16 and Country="India"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i                                 
                    elif(sel_field_coach_iq==1 and sel_field_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Improvement_Quotient>6 and Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_iq==1 and sel_field_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Improvement_Quotient>6 and Country="India"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_hpw==1 and sel_field_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Country="India" and Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_iq==1 and sel_field_coach_count==1 and sel_field_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Country="India" and Hours_per_week>16 and Improvement_Quotient>6')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_iq==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Improvement_Quotient>6')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_hpw==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Hours_per_week>16')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    elif(sel_field_coach_count==1):
                        mylist.delete(first,last)
                        first=0
                        cur.execute('SELECT * FROM Fielding_coach WHERE Country="India"')
                        i=1
                        mylist.insert(0,"COACH ID     HPW         IQ            Country            Coach name")
                        for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[3])+"                "+str(row[4])+"          "+str(row[2])+"                "+str(row[1]))      
                        last=i
                    else:
                        mylist.delete(first,last)
                        first=0
                        mylist.insert(0,"NULL")
                        last=0

                           
                root.geometry("1000x600")

                frame25=Frame(root)
                frame26=Frame(root)
                frame27=Frame(root)
                frameb=Frame(root)
                
                frame14.destroy()
                frame15.destroy()

                frame25.place(x=0,y=0,height=600,width=400)
                frame26.place(x=400,y=0,height=500,width=600)
                frame27.place(x=500,y=500,height=50,width=400)
                frameb.place(x=500,y=550,height=50,width=400)

                cb31=Checkbutton(frame25,text="Select All",onvalue=1,offvalue=0,height=5,width=20,command=sel_all)
                cb32=Checkbutton(frame25,text="Country='India'",onvalue=1,offvalue=0,height=5,width=20,command=sel_country)
                cb33=Checkbutton(frame25,text="Hours Per Week>16",onvalue=1,offvalue=0,height=5,width=20,command=sel_hpw)
                cb34=Checkbutton(frame25,text="Improvement Quotient>6",onvalue=1,offvalue=0,height=5,width=20,command=sel_iq)
                go=Button(frame25,text="search",command=search)
                cb31.pack()
                cb32.pack()
                cb33.pack()
                cb34.pack()
                go.pack()

                scroll=Scrollbar(frame26)
                scroll.pack(side=RIGHT,fill=Y)

                mylist=Listbox(frame26,height=400,width=400,yscrollcommand=scroll.set)
                scroll.config(command=mylist.yview)
                mylist.pack(side=LEFT,fill=BOTH)

                user=Label(frame27,text="Coach Id:")
                user.pack(side=LEFT)
                insert=Entry(frame27,textvariable=ID_field_coach)
                insert.pack(side=RIGHT)
                add=Button(frameb,text="ADD",command=add_coach)
                add.pack(side=LEFT)
                back=Button(frameb,text="BACK",command=back)
                back.pack(side=RIGHT)

            def back():
                frame14.destroy()
                frame15.destroy()
                start()
                        
            root.geometry("800x100")
            frame3.destroy()
            frame4.destroy()

            frame14=Frame(root)
            frame15=Frame(root)
            frame14.pack()
            frame15.pack()

            label1=Label(frame14,text="COACHES")
            label1.pack()

            button_bat=Button(frame15,text="Batting Coach",command=bat_coach)
            button_bat.grid(row=3,column=0) 
            button_ball=Button(frame15,text="Bowling Coach",command=ball_coach)
            button_ball.grid(row=3,column=1)
            button_field=Button(frame15,text="Fielding Coach",command=field_coach)
            button_field.grid(row=3,column=2)
            button_coach=Button(frame15,text="Back",command=back)
            button_coach.grid(row=4,columnspan=3)

        def view():                
            def remove_player():
                def display(lastz):
                    global first
                    global last
                    mylist.delete(first,lastz+1)
                    first=0
                    cur.execute('Select * from Team')
                    i=1
                    mylist.insert(0,"PLAYER ID     CODE                             NAME")
                    for row in cur:
                            i=i+1
                            mylist.insert(i,str(row[0])+"              "+str(row[2])+"                                     "+str(row[1]))      
                    last=i
                num=ID_play.get()                
                global player_count
                global bats_count
                global balls_count
                global field_count
                cur1.execute('Select code from Team where Player_id=?',(num,))
                for row in cur1:
                    if(row[0]==0):
                        bats_count=bats_count-1
                    elif(row[0]==1):
                        balls_count=balls_count-1
                    else:
                        field_count=field_count-1    
                cur.execute('Delete from Team where Player_id=?',(num,))
                cur.execute('Select count(*) from team')
                for row in cur:
                    display(row[0])
                player_count=player_count-1

            def remove_coach():
                def display(lastz):
                    global first
                    global last
                    mylist1.delete(first,lastz+1)
                    first=0
                    cur.execute('Select * from Coach')
                    i=1
                    mylist1.insert(0,"COACH ID     CODE                             NAME")
                    for row in cur:
                            i=i+1
                            mylist1.insert(i,str(row[0])+"              "+str(row[2])+"                                     "+str(row[1]))      
                    last=i
                num=COACH_ID.get()                
                global coach_count
                global bat_count_coach
                global ball_count_coach
                global field_count_coach
                cur1.execute('Select code from Coach where Coach_id=?',(num,))
                for row in cur1:
                    if(row[0]==0):
                        bat_count_coach=bat_count_coach-1
                    elif(row[0]==1):
                        ball_count_coach=ball_count_coach-1
                    else:
                        field_count_coach=field_count_coach-1
                cur.execute('Delete from Coach where Coach_id=?',(num,))
                cur.execute('Select count(*) from coach')
                for row in cur:
                    display(row[0])
                coach_count=coach_count-1
                
            def go_back():
                frame16.destroy()
                frame17.destroy()
                frame18.destroy()
                framet.destroy()
                framem.destroy()
                start()
            
            root.geometry("700x600")
            
            frame16=Frame(root)
            frame17=Frame(root)
            frame18=Frame(root)
            framet=Frame(root)
            framem=Frame(root)

            frame3.destroy()
            frame4.destroy()

            frame16.place(x=0,y=0,height=400,width=500)
            frame17.place(x=500,y=0,height=200,width=200)
            frame18.place(x=500,y=200,height=200,width=200)
            framet.place(x=0,y=400,height=300,width=500)
            framem.place(x=500,y=400,height=200,width=200)
            

            scroll=Scrollbar(frame16)
            scroll.pack(side=RIGHT,fill=Y)

            mylist=Listbox(frame16,height=400,width=500,yscrollcommand=scroll.set)
            scroll.config(command=mylist.yview)
            mylist.pack(side=LEFT,fill=BOTH)

            scroll=Scrollbar(framet)
            scroll.pack(side=RIGHT,fill=Y)

            mylist1=Listbox(framet,height=300,width=500,yscrollcommand=scroll.set)
            scroll.config(command=mylist.yview)
            mylist1.pack(side=LEFT,fill=BOTH)

            remove=Button(frame17,text="remove",command=remove_player)
            labelx=Label(frame17,text="Player Id")
            delete=Entry(frame17,textvariable=ID_play)
            labelx.grid(row=50,column=0)
            delete.grid(row=50,column=1)
            remove.grid(row=51,columnspan=2)

            back=Button(frame18,text="Return",command=go_back)
            back.pack()

            remove=Button(framem,text="remove",command=remove_coach)
            labelx=Label(framem,text="Coach Id")
            delete_coach=Entry(framem,textvariable=COACH_ID)
            labelx.grid(row=50,column=0)
            delete_coach.grid(row=50,column=1)
            remove.grid(row=51,columnspan=2)

            global first
            global last
            mylist.delete(first,last)
            first=0
            cur.execute('Select * from Team')
            i=1
            mylist.insert(0,"PLAYER ID     CODE                             NAME")
            for row in cur:
                    i=i+1
                    mylist.insert(i,str(row[0])+"              "+str(row[2])+"                                     "+str(row[1]))      
            last=i

            mylist1.delete(first,last)
            first=0
            cur.execute('Select * from Coach')
            i=1
            mylist1.insert(0,"COACH ID     CODE                             NAME")
            for row in cur:
                    i=i+1
                    mylist1.insert(i,str(row[0])+"              "+str(row[2])+"                                     "+str(row[1]))      
            last=i
            
        frame1.destroy()
        frame2.destroy()

        frame3=Frame(root)
        frame4=Frame(root)
        frame3.pack()
        frame4.pack()

        label1=Label(frame3,text="Welcome "+name.get())
        label1.pack()

        button_bat=Button(frame4,text="Batsman",fg='Green',command=batsmen)
        button_bat.grid(row=3,column=0)
        button_ball=Button(frame4,text="Bowler",fg='Red',command=bowlers)
        button_ball.grid(row=3,column=1)
        button_field=Button(frame4,text="Fielder",fg='Blue',command=fielders)
        button_field.grid(row=3,column=2)
        button_coach=Button(frame4,text="Coaches",fg='Orange',command=coaches)
        button_coach.grid(row=3,column=3)
        button_team=Button(frame4,text="View Team",fg='Purple',command=view)
        button_team.grid(row=4,columnspan=4)
    
    root.geometry("800x100")
    frame1=Frame(root)
    frame2=Frame(root)
    frame1.pack()
    frame2.pack(side=BOTTOM)

    label1=Label(frame1,text="CRICKET FANTASY XI")
    label1.pack()

    label2=Label(frame2,text="User Name:",fg='Brown')
    label2.grid(row=1,column=0)
    entry=Entry(frame2,textvariable=name)
    entry.grid(row=1,column=1)
                
    button=Button(frame2,text="Start",fg='Maroon',command=start)
    button.grid(row=2,columnspan=2)

create_tables()
login()

root.mainloop()
