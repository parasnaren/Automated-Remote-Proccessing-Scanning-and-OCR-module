from webbot import Browser
web = Browser()

web.go_to('http://www.myvehicledetails.com/')


web.type('MAKGM263CAN100883' , tag='input')
web.click('submit' , tag='button') # you are logged in ^_^

#<button class="aOOlW   HoLwm " tabindex="0">Not Now</button>
# <button class="aOOlW   HoLwm " tabindex="0">Not Now</button>
