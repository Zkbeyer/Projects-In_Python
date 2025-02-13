# get a string input for file name
def inputFileString(prompt):
    f = None
    while True:
        s = str(input(prompt))
        try:
            f = open(s,'r')
        except Exception as error:
            print(error)
        else:
            break
    if f!= None:
        f.close
    return s


#count total songs
def countSongs(file_name):
    file = None
    count = 0
    try:
        file = open(file_name, 'r', encoding="utf-16")
        #count the rows in the data, subtracting the header
        for rows in file:
            count += 1
        if count > 0:
            count -= 1
    except Exception as error:
        print(error)
    finally:
        if(file != None):
            file.close
        return count

#counts the songs per year
#song year is found at index 16
def countSongsByYear(file_name):
    file = None
    count = {}
    try:
        file = open(file_name, 'r', encoding="utf-16")
        for lines in file:
            song = lines.split("\t") #parses the data to be readable
            if song[16] == '' or song[16] == 'Year':
                continue
            if song[16] in count:
                count[song[16]] += 1
            else:
                count[song[16]] = 1
    except Exception as error:
        print(error) 
    finally:
        if(file != None):
            file.close
        return count

#finds longest song
#index for Time is 11
def findLongestSong(file_name):
    time = 11
    
    file = None
    largest = None
    final = []
    try:
        file = open(file_name, 'r', encoding="utf-16")
        for lines in file:
            song = lines.split("\t") #parses the data to be readable
            if song[1] == '':
                song[1] = "Unknown"
            if str(song[time]) == 'Time' or song[time] == '':
                continue
            song_int = int(song[time])
            #keeps track of the largest time, if there is a bigger time, insert new song
            if largest == None:
                largest = song_int
            if song_int > largest:
                largest = song_int
                final.clear()
                final.append(song[0] + ', ' + song[1])
            elif song_int == largest:
                final.append(song[0] + ', ' + song[1])
    except Exception as error:
        print(error) 
    finally:
        if(file != None):
            file.close
        return final

#find shortest song
#index for time is 11
def findShortestSong(file_name):
    #indexes for information
    time = 11
    
    file = None
    smallest = None
    final = []
    try:
        file = open(file_name, 'r', encoding="utf-16")
        for lines in file:
            song = lines.split("\t")#parses the data to be readable
            #Pre conditions to make sure the data were reading is usable
            if song[1] == '':
                song[1] = "Unknown"
            if str(song[time]) == 'Time':
                continue
            if str(song[time]) == '':
                continue
            
            song_int = int(song[time])
            if smallest == None:
                smallest = song_int
            
            if song_int < smallest:
                smallest = song_int
                final.clear()
                final.append(song[0] + ', ' + song[1])
            elif song_int == smallest:
                final.append(song[0] + ', ' + song[1])
    except Exception as error:
        print(error) 
    finally:
        if(file != None):
            file.close
        return final


#Find information for each genre
#index for genre is 9
def getGenreData(file_name):
    #indexes for information
    genre = 9
    name = 0
    artist = 1
    time = 11
    
    file = None
    genre_list = {}
    #genre [count, longest[name, artist, time], shortest[name, artist, time]]
    try:
        file = open(file_name, 'r', encoding="utf-16")
        for lines in file:
            song = lines.split("\t")
            if song[genre] == "Genre":
                continue
            #if its a new genre add it to the dictionary
            if song[genre] not in genre_list:
                genre_list[song[genre]] = [1, [[song[name], song[artist], song[time]]],[[song[name], song[artist], song[time]]]]
            #if its not a new genre make sure its not the longest or shortest
            elif song[genre] in genre_list:
                genre_list[song[genre]][0] += 1
                if song[time] == '':
                    continue
                #checking largest
                if int(genre_list[song[genre]][1][0][2]) < int(song[time]):
                    genre_list[song[genre]][1] = [[song[artist],song[name],song[time]]]
                elif int(genre_list[song[genre]][1][0][2]) == int(song[time]):
                    genre_list[song[genre]][1].append([song[artist],song[name],song[time]])
                #checking shortest
                if int(genre_list[song[genre]][2][0][2]) > int(song[time]):
                    genre_list[song[genre]][2] = [[song[artist],song[name],song[time]]]
                elif int(genre_list[song[genre]][2][0][2]) == int(song[time]):
                    genre_list[song[genre]][2].append([song[artist],song[name],song[time]])
                    
    except Exception as error:
        print(error) 
    finally:
        if(file != None):
            file.close
    return genre_list

#how many songs have been played
#index for played songs is 25
def songsPlayed(file_name):
    plays = 25
    file = None
    count = 0
    try:
        file = open(file_name, 'r', encoding="utf-16")
        for lines in file:
            song = lines.split("\t")
            if song[plays] == "Plays" or song[plays] == "":
                continue
            if int(song[plays]) > 0:
                count += 1
    except Exception as error:
        print(error) 
    finally:
        if(file != None):
            file.close
        return count

#how many songs have not been played
#index for played songs is 25
def songsNotPlayed(file_name):
    plays = 25
    file = None
    count = 0
    try:
        file = open(file_name, 'r', encoding="utf-16")
        for lines in file:
            song = lines.split("\t")
            if song[plays] == "Plays":
                continue
            if song[plays] == "":
                count += 1
    except Exception as error:
        print(error) 
    finally:
        if(file != None):
            file.close
        return count

#to display a variable
def display(var, prompt):
    print(" ")
    print(prompt)
    print(var)
    

#to display a basic dictionary
def displayDictionary(dictionary, prompt):
    print(" ")
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: int(item[0])))
    print(prompt)
    for key, value in sorted_dict.items():
        print(str(key) + ": " + str(value))

#to display a basic list
def displayList(l, prompt):
    print(" ")
    print(prompt)
    for items in l:
        print(items)

#Display the genre information (specifically for getGenreData())
def displayGenreData(genre_list, prompt):
    print(" ")
    print(prompt)
    print(" ")
    sorted_dict = dict(sorted(genre_list.items(), key=lambda item: int(item[1][0])))
    for genre in genre_list:
        print(" ")
        print("-----" + str(genre) + "(" + str(genre_list[genre][0])+")-----")#prints genre header
        print(" ")
        #print all the longest songs in the list
        print('Longest: ')
        for longest in genre_list[genre][1]:
            if longest[1] == '':
                longest[1] = "Unknown"
            if longest[0] == '':
                longest[0] = "Unknown"
            print(str(longest[1]))
            print('By: ' +str(longest[0]))

        print(" ")

        #print all the shortest songs in the list
        print('Shortest: ')
        for shortest in genre_list[genre][2]:
            if shortest[1] == '':
                shortest[1] = "Unknown"
            if shortest[0] == '':
                shortest[0] = "Unknown"
            print(str(shortest[1]))
            print('By: ' +str(shortest[0]))
 

#to display the input for getting file_name
def getFileName():
    print(" ")
    file_name = inputFileString("Inptut File Name: ")
    print(" ")
    return file_name

# displays all the music information for a provided file
def displayMusicData():
    file_name = getFileName()
    display(countSongs(file_name), "-----SONG COUNT-----")
    displayDictionary(countSongsByYear(file_name), "-----SONGS BY YEAR-----")
    displayList(findLongestSong(file_name), "-----LONGEST SONGS-----")
    displayList(findShortestSong(file_name), "-----SHORTEST SONGS-----")
    displayGenreData(getGenreData(file_name), "-----GENRE DATA-----")
    display(songsPlayed(file_name), "-----SONGS PLAYED-----")
    display(songsNotPlayed(file_name), "-----SONGS NOT PLAYED-----")
            
    
#main function
def main():
    print("----------MUSIC ANALYZER------------")
    #Allows multiple inputs until the user says no
    while True:
        print(" ")
        displayMusicData()
        print(" ")
        again = str(input("Would You Like To Scan Another Music File? (y/n): "))
        if again == "n" :
            return

main()
    
