import sqlite3
import time



conn =sqlite3.connect('ytmanager.db')
cursor = conn.cursor()


cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   TIME TEXT NOT NULL
               )

               ''')

def list_all_videos():
     cursor.execute("SELECT * FROM videos")
     for row in cursor.fetchall():
          print(row)
    


def add_video(name, time):
     cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
     conn.commit()

def update_video(video_id,new_name, new_time):
     cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
     conn.commit()

def delete_video(video_id):
     cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
     conn.commit()




def main():
    

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        if choice == '1':
            list_all_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video( name, time)

        elif choice == '3':
            video_id = int(input("Enter video id to update: "))
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video time: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = int(input("Enter video id to delete: "))
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice") 
    # print(videos)                


if __name__ == "__main__":
            main()