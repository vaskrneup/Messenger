## Installation
Messenger runs on Python 3.6 or greater:

Run the following command to install required packages.

```sh
pip install -r req.txt
```

```python
    # you can copy the url of particular user from messenger.com !!
    # You need to download selenium web driver for this to work !!
    # you can download driver for your preferred browser here:
    # https://selenium-python.readthedocs.io/installation.html
    messenger = Messenger(
        "https://www.messenger.com/t/<USERNAME>",
        driver_path="<DRIVER PATH>"
    )
    # Login Using your facebook credentials !!
    messenger.login("<USERNAME>", "<PASSWORD>")
    # user use_random_message=True to send random message.
    # You can use message count to specify how many message you wish to send.
    messenger.send_message(use_random_message=True, message_count=100)
    # You can also send specific message !!
    messenger.set_messages(["you can", "specify any", "Number of messages."])
    # send the message from set_messages !!
    messenger.send_message()
    # close after everything is completed !!
    messenger.close()
```
