Tambola Stage 4 - Win the game
======================
In this activity, you will display the winner or loser in the game.
<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525744/images/8813171/prjct.png" width = "100%" height = "50%">

Follow the given steps to complete this activity.

1. Display the winner.
* Open the file “client.py” and go to method mark_number(button).
* Check if all the items in flash_number_list exits in marked_number_list and return the result to the winner variable


```
winner =  all(item in flash_number_list for item in marked_number_list)
```
* Check if we have a winner. If true, create the winning message, send it to the server, and return it.




```
if(winner and sorted(current_number_list) == sorted(marked_number_list)):
        message = player_name + ' wins the game.'
        SERVER.send(message.encode())
        return
```


2. Display the losing message.
* Check for the winner by first checking if the length of current_number_list is equal to marked_number_list. If yes, check if all items in flash_number_list exits in marked_number_list and return the result to the winner variable


```
if(len(current_number_list) == len(marked_number_list)):
     winner =  all(item in flash_number_list for item in marked_number_list)


```
* If the winner is not true, display the losing message. 
```
if(not winner):
     gameOver = True
     message = 'You Lose the Game'
     canvas2.itemconfigure(flash_number_label, text = message, font = ('Chalkboard SE', 40))
     show_wrong_marking()
```


* Save and run the code by first running the server.py and then client.py to check the output.
