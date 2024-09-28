import sqlite3

conn =sqlite3.connect("youtube.db")

cursor =conn.cursor()

cursor.execute('''
    CURSOR TABLE IF NOT EXITS  videos(
               id INTEGERS PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time )VALUES(?,?)",(name,time))
    conn.commit


def updata_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name=?,time=?,WHERE id=? ",(name,time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id=?",(video_id,))
    conn.commit()


def main():
    while True:
        print("!! YOUTUBE VIDEO MANAGER !! ")
        print("1: List of all Youtube Video :")
        print("2: Add a youtube video: ")
        print("3: Update a youtube Video: ")
        print("4: Delete a Youtube Video: ")
        print("5: Exit the app")
        choice = input("enter the coice ")

    if choice=='1':
        list()


    elif choice==2:
       name= input("enter the vedio name ")
       time=input("enter the time ")
       add_video(name, time)

    elif choice==3:
        vedio_id=input("enter the vedio id ")
        name=input("enter the video name ")
        time=input("enter the time ")
        updata_video(vedio_id,name,time)

    elif choice==4:
        video_id= input("enter the video to delete")
        delete_video(video_id)

    # elif choice==5:
    #     break:

    else:
        print("enter the valid")

if __name__=="__main__":
    main()