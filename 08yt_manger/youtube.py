import json 
def load_data():
    try:
        with open('youtube.txt','r') as file:
           
           return json.load(file)
    except FileNotFoundError:
                 return []
       

def save_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file,indent=4)


def list_all_videos(videos):
     for i, video in enumerate(videos, start=1):
        print(f"{i}. {video['name']} - Duration: {video['duration']}")
   
    #  exit()   


def add_video(videos):
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")
    videos.append({'name': name, 'duration': duration})
    save_helper(videos)

   
def update_video(videos):
    list_all_videos(videos)
    index =int(input("enter the video number to update "))
    if(1 <= index <= len(videos)):
        name = input("Enter new video name: ")
        duration = input("Enter new video duration: ")
        videos[index-1] = {'name': name, 'duration': duration}
        save_helper(videos)
    
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        videos.pop(index - 1)
        save_helper(videos)
    pass

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
    # print(videos)                


if __name__ == "__main__":
            main()