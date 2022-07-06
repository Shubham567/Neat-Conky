## C137 Rick & Morty Neat Conky

Neat, Rick & Morty based conky theme for your Linux desktop.
See quick preview - preview.png

[Neat conky preview c137 rick & morty](./preview.png)

### Update :
*   Added support for conky manager.

*   Replaced signature to show a random computer science        quote from a pool of 350 quote updates once every 10        mins. Requires python3 installed.
*   Reduced refresh rate by 0.1 sec. Now updates twice          every second.

### Features:
   * The center line is: Hey Rick This is {username logged in}!

   * All the stats including graphs, except for Filesystem and Others turn red when usage is too high. Example Image

   * Live feeds from Reuters RSS feed.

   * The last line(signature) gets replaced by Battery Low warning when battery is less than 15%.

   * Signature is read from file called signature.txt modify it to edit the last line of theme.

   * Signature section is now modified to show a random quote.

### How to add this theme to conky-manager?

Run the following command,

> `$ mkdir ~/conky-themes ~/conky-themes/Neat` <br>
> `$ git clone https://github.com/Shubham567/Neat-Conky.git ~/conky-themes/Neat`

Open Conky Manager, Go to settings and add location ~/conky-themes. Run the theme.



### How to change signature(last line of theme)?
Initially it was hard coded. Now onwards it will read the first line as status from file signature.txt included in the folder. 
To change it simply put a text you want to show. You can use your script to generate the text file.
It refreshes once every 10 min. You can change the refresh rate by editing "Time" file.

### Issues:
Currently works with nvidia graphics card only. I am trying to add Intel as well. I dont have AMD so cant be sure If I did it correctly so I wish I could get some help. Contributers are welcomed.

Sorry for putting my signature in there at last. Couldnt come up with an ending line. Hope you will do better. You can change it by editing signature.txt.

##### Soon adding more running methods

##### Customization of Jesse Time Conky theme. But I think I added too much to call it just a customization now.
