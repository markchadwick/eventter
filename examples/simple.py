from eventter import send, on_message, remove_callback
import time

def listener(title, message):
    print '- ' * 30
    print 'Title:  ', title
    print 'Message:', message
    
if __name__ == '__main__':
    on_message(listener)
    send(title='A Message Title', message='Check out this message!')
    
    time.sleep(1)
    
    remove_callback(listener)