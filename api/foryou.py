import json

class Activity:
    def __inti__(activity, name, hobby, price, duration):
        activity._name = name
        activity._hobby = hobby
        activity._price = price
        activity._duration = duration
        
@property 
def activity(activity):
    return activity._name

@activity.setter
def activity(activity, name):
    activity._name = name 
    
@property
def hobby(activity):
    return activity._hobby

@hobby.setter
def hobby(activity, hobby):
    activity._hobby = hobby
    
@property
def price(activity):
    return activity._price

@price.setter
def price(activity, price):
    activity._price = price
    
@property
def duration(activity):
    return activity._duration

@duration.setter
def duration(activity, duration):
    activity._duration = duration
    
# output content using str(object) in human readable form, uses getter
    def __str__(activity):
        return f'name: "{activity.name}", hobby: "{activity.hobby}", price: "{activity.price}", duration: "{activity.duration}"'
    
# output command to recreate the object, uses attribute directly
    def __repr__(activity):
        return f'Activity(name={activity._name}, hobby={activity._hobby}, price={activity._price}, duration={activity._duration})'

if __name__ == "__main__":
    
    #define activity objevts
    a1 = Activity(name='SeaWorld', hobby='Amusement Park', price= '$100-$200', duration= 'all-day')

# pur user objects in list for convenience
activities = [a1]

print(str(activity))
