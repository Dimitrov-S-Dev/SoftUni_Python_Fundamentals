"""
You will receive a journal with some Collecting items,
separated with ", " (comma and space).
After that, until receiving "Craft!"
you will be receiving different commands.
Commands (split by " - "):
· "Collect - {item}" – Receiving this command,
you should add the given item to your inventory.
If the item already exists, you should skip this line.
· "Drop - {item}" – You should remove the item from your inventory
if it exists.
· "Combine Items - {oldItem}:{newItem}"
You should check if the old item exists.
If so, add the new item after the old one. Otherwise, ignore the command.
· "Renew – {item}" – If the given item exists,
you should change its position and put it last in your inventory.
"""


