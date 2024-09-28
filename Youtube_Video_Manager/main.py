import json

def load_data():
    try:
        with open ("youtube.txt" ,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [1,3]
    
def helper(video):
    with open('youtube.txt', 'w') as file:
        json.dump(video ,file)

def  list_of_all(video):
    for index , video in enumerate(video , start=1):
        print (f"{index} .{video['name']},Duration: {video['time']}")

def add_video(video):
    name=input("what is your video name")
    time=input("what does time you want to set ")
    video.append({'name': name , 'time':time})
    helper(video)

def update_video(video):
    index=int(input("enter the video number to update"))
    if 1<=index <= len(video):
        name=input("enter the new")
        time=input("enter the time")
        video[index-1]={'name' :name , 'time':time }
        helper()
    else:
        print("enter the valid number")

def delete_video(video):
    list_of_all(video)
    index= int(input("enter the video number"))

    if 1<=index  <= len(video):
        del video[index-1]
        helper()

    else:
        print("enter the valid number")




def main():
    video =load_data()
    while True:
        print("!! YOUTUBE VIDEO MANAGER !! ")
        print("1: List of all Youtube Video :")
        print("2: Add a youtube video: ")
        print("3: Update a youtube Video: ")
        print("4: Delete a Youtube Video: ")
        print("5: Exit the app")
        choice = input("enter the coice")

        match choice:
            case '1':
                list_of_all(video)

            case '2':
                add_video(video)

            case '3':
                update_video(video)

            case '4':
                delete_video(video)

            case '5':
                break

            case __:
                print("invalid number")

if __name__== "__main__":
    main()