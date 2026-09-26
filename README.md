# bon-burger-tracker
A simple webscraping script connected to a Twitter bot.
My home server runs bot.py every day at 9 A.M., checking whether burgers appear on the Fields Dining Room menu anytime in the next 14 days.
On  the Bon Appétit website, users can normally view the menu for the next seven days. However, the menu for any date can be viewed by simply changing the url manually instead of using the UI:

`https://lewisandclark.cafebonappetit.com/cafe/fields-dining-room/YYYY-MM-DD/`

Sometimes the menu is set for days more than one week away, which is why I set the bot to search the next 14 days for burgers. 
