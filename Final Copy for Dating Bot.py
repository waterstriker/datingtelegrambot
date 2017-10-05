import sys
import time
import os
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import pave_event_space, per_chat_id, create_open
# Import InlineKeyboardMarkup, InlineKeyboardButton to use keyboard buttons.
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
# Import delegator bot and included include_callback_query_chat_id so buttons can be implemented in delegator bot.
from telepot.delegate import (
    per_chat_id, create_open, pave_event_space, include_callback_query_chat_id)


# Read the text file addfile.txt and extracts and saves dictionary address_dict with key as the name of the recreation activity and value as address of the activity.
file = open(os.path.expanduser('~\\Desktop') + "\\addfile.txt", 'rb')
content = file.read()
address_dict=eval(content.decode("utf-8"))
file.close()

# Read the text file telfile.txt and extracts and saves dictionary contactNumber_dict with key as the name of the recreation activity and value as telephone numebrs of the activity.
file = open(os.path.expanduser('~\\Desktop') + "\\telfile.txt", 'rb')
content = file.read()
contactNumber_dict=eval(content.decode("utf-8"))
file.close()

# Read the text file descfile.txt, extracts and saves description_dict with key as the name of the recreation activity and value as description of the activity.
file = open(os.path.expanduser('~\\Desktop') + "\\descfile.txt", 'rb')
content = file.read()
description_dict=eval(content.decode("utf-8"))
file.close()

# Read the text file descfile.txt, extracts and saves activityname_list with the names of the recreation activity.
file = open(os.path.expanduser('~\\Desktop') + "\\activityname.txt", 'rb')
content = file.read()
activityname_list=eval(content.decode("utf-8"))
file.close()

# Read the text file telfile.txt and extracts and saves dictionary c_restaurant_address_dict with key as the name of the restaurant and value as address of the restaurant.
file = open(os.path.expanduser('~\\Desktop') + "\\c_restaurant_address.txt", 'rb')
content = file.read()
c_restaurant_address_dict=eval(content.decode("utf-8"))
file.close()

# Read the text file descfile.txt, extracts and saves casual_description_dict with key as the name of the restaurant and value as description of the restaurant.
file = open(os.path.expanduser('~\\Desktop') + "\\c_restaurant_desc.txt", 'rb')
content = file.read()
casual_description_dict=eval(content.decode("utf-8"))
file.close()

# Read the text file descfile.txt, extracts and saves c_restaurant_names_list with the names of the restaurant.
file = open(os.path.expanduser('~\\Desktop') + "\\c_restaurant_names.txt", 'rb')
content = file.read()
c_restaurant_names_list=eval(content.decode("utf-8"))
file.close()

# The purpose of MessageCounter is allow the program to know which step and what actions should be carried out by our bot.
class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)
        self._count = 0
        
    # When the keyboard is selected by the user, on_callback_query will run.
    # Our Bot Program starts from step 1, Line .
    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

        # Step 2: User has selected a type of dating activity.
        if self._count==1:

            # Variable self.option saves the type of dating option selected by the user.
            self.option = query_data
            
            if self.option =='Eat' or self.option == 'Recreation':
                # Prints the message that the user has selected this type of dating option.
                self.sender.sendMessage('You have selected: '+self.option)
                # Moves on to next step, which is step 3, Line  .
                self._count+=1
                # Prints the message to type go to continue
                self.sender.sendMessage('Type go to continue. Type anything else to select another dating option.')

            # Tells user that the key selected is not in the optionkeyboard(Line ), and prompts a selection from the user again.
            else:
                self.sender.sendMessage("Invalid input. Please try again.")

        # Step 4: To check if user has selected the valid name of a dating activity or the user has selected the option of eating at a casual outlet.
        elif self._count==3:
                                        
            # Variable self.choice saves the name of recreaion activity or type of eating option selected by the user.
            self.choice = query_data
            
            if self.choice in activityname_list:
                # Prints out message that user has selected this recreaion activity
                self.sender.sendMessage("You have selected: "+self.choice)
                # Moves on to next step, which is step 5, Line 
                self._count+=1
                # Prints out message to type go to continue
                self.sender.sendMessage("Type go to continue. Type anything else to select another dating activity.")

            elif self.choice =='Casual':

                # Prints out message that user has selected this eating option for a date
                self.sender.sendMessage("You have selected: "+self.choice)
                # Moves on to next step, which is step 5, Line 
                self._count+=1
                # Prints out message to type go to continue
                self.sender.sendMessage("Type casualeat to continue. Type anything else to select another dating activity.") 

            # Tells user that the key selected is not the name of recreaion activity or type of eating option, and prompts a selection from the user again.
            else:
                self.sender.sendMessage("Invalid input. Please try again.")
                
        # Step 6:  This steps consist of two functions.
        # 1) Information for the recreation activity selected by user will be shown. This information will include Address, Contact number and Description of Recreation Activity.
        # It also allows user to restart the bot.(Applicable only when restarting the bot after looking through the information for the recreation activity.
        # 2) To check if the user has selected the valid name of a casual outlet.
        elif self._count==5:
            
            # The variable self.information is assigned the number which corresponds to address,contact numbers, description of dating activities and restarting the bot respectively.
            
            self.information = query_data
        
            # If self.information is given the value 1, it will prints the address of the activity the user has choosen.
            if self.information == "1":
                self.sender.sendMessage("Here is the address for "+self.choice+":\n"+self.address)
            
            # If self.information is given the value 2, it will print the contact numbers of the activity which the user has choosen.
            elif self.information == "2":
                self.sender.sendMessage("Here is the contact number for "+self.choice+":\n"+self.contactNumber)
            
            # If self.information is given the value 3, it will print the description of the activity which the user has choosen.
            elif self.information == "3":
                self.sender.sendMessage("Here is the description of activity for "+self.choice+":\n"+self.description)
            
            # If self.information is given the value 4, the bot will restart itself.    
            elif self.information == "4":
                self._count = 0
                self.sender.sendMessage("Bot has restarted. Type anything to proceed.")

            elif self.information in c_restaurant_names_list:
                
                self.sender.sendMessage("You have selected: "+self.information)
                # Moves on to next step, which is step 7, Line 
                self._count+=1
                # Prints out message to type casualeat to continue
                self.sender.sendMessage("Type casualeat to continue. Type anything else to select another dating activity.")
                
            # If self.information is given the value not provided by the bot, the bot will inform the user to make a valid selection.
            else:
                self.sender.sendMessage("The information you selected is not available. Please try again.")

        # Step 8: Information for the causal outlet selected by user will be shown. This information will include Address and Description of Casual Outlet.
        # It also allows user to restart the bot.
        elif self._count==7:
            
            # The variable self.option is assigned the number which corresponds to address, description of casual restaurants and restarting the bot respectively.
            
            self.option = query_data
        
            # If self.option is given the value 1, it will prints the address of the restaurant the user has choosen.
            if self.option == "1":
                self.sender.sendMessage("Here is the address for "+self.information+":\n"+self.address)
            
            # If self.option is given the value 2, it will print the description of the restaurant which the user has choosen.
            elif self.option == "2":
                self.sender.sendMessage("Here is the description of restaurant for "+self.information+":\n"+self.description)
            
            # If self.option is given the value 3, the bot will restart itself.    
            elif self.option == "3":
                self._count = 0
                self.sender.sendMessage("Bot has restarted. Type anything to proceed.")

    # When the user types any message, on_chat_message will run.
    def on_chat_message(self, msg):
        
        # Step 1: The Bot will introduces himself and provide two type of dating option for user to select from.
        if self._count==0:

            # optionkeyboard will produce the buttons for user to select his/her preferred dating option.
            global optionkeyboard
            
            optionkeyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Eat', callback_data='Eat')],[InlineKeyboardButton(text='Recreation',callback_data='Recreation')]])

            # Prints the bot's objective for the user
            self.sender.sendMessage('Hello, I am a bot who is here to help you to plan a date! ^^')

            # The program is paused for 3 seconds for user to read the message.
            time.sleep(3)
            
            # Prints the datiing options for users to choose from.
            self.sender.sendMessage('Please select the type of dating option:', reply_markup=optionkeyboard)
            # Moves to step 2, Line .
            self._count+=1



        # Step 3: 1) Shows the dating activities for the dating option:'Recreation', and prompts user to select one activty for more information.
        # 2) Prompts the user to select either eating at a casual outlet or formal restaurant.
        elif self._count==2:
            
            # To ensure that the user has typed go and has selected the dating option: Recreation in order to move on to next step.
            if msg['text'].lower()=='go' and self.option=='Recreation':

                # Create a activitykeyboard and activitymarkup which has the names of dating activities for the user to select from.                        
                activitykeyboard=[]
                for activityname in activityname_list:
                    activitykeyboard.append([InlineKeyboardButton(text=activityname, callback_data=activityname)])
                global activitymarkup
                activitymarkup= InlineKeyboardMarkup(inline_keyboard= activitykeyboard)

                # Prints the names of activities for users to choose from.
                self.sender.sendMessage('Here is a list of dating activities to do in Singapore for fun! Please select one:', reply_markup=activitymarkup)
                self.sender.sendMessage('Please select the activity provided')

                #Moves to step 4, Line .
                self._count+=1
                
            # To ensure that the user has typed go and has selected the dating option: Eat in order to move on to next step
            elif msg['text'].lower()=='go' and self.option=='Eat':

                # eating_choicekeyboard will produce the buttons for user to select his/her preferred eating option for his date.
                global eating_choicekeyboard
            
                eating_choicekeyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Casual', callback_data='Casual')],[InlineKeyboardButton(text='Formal',callback_data='Formal')]])

                # Prints the eating options for users to choose from.
                self.sender.sendMessage('Please select the type of eating option:', reply_markup=eating_choicekeyboard)

                #Moves to step 4, Line .
                self._count+=1

            # If the user did not type go, bot will execute these steps.
            else:
                #Prints the message informing the user that he/she did not type go.
                self.sender.sendMessage('You did not type go. Please select again.')
                # time delay 1 second.
                time.sleep(1)              

                # Prints the names of activities for users to choose from again.
                self.sender.sendMessage('Please select the type of dating option:', reply_markup=optionkeyboard)
                #Moves back to step 2, Line 
                self._count-=1
              

        # Step 5: 1) Shows the information for the activity selected by the user.
        #         2) Shows the names of casual outlets for the user for the user to choose from.
        elif self._count==4:

            # To ensure that the user has typed go
            if msg['text'].lower()=='go':
                # variable informationkeyboard is a list with information such as 1. Address, 2. Contact number, 3. Description of activity, or 4. Try planning another date. 
                informationkeyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Address', callback_data='1')],[InlineKeyboardButton(text='Contact Number', callback_data='2')],[InlineKeyboardButton(text='Description of Activity', callback_data='3')],[InlineKeyboardButton(text='Try Planning Another Date', callback_data='4')]])
                self.sender.sendMessage('This is the list of information for the activity you have chosen: \n',reply_markup=informationkeyboard)
                self.sender.sendMessage('Please use the keyboard provided.')
                                           
                # Variables from line  to line  are assigned values based on 1.address, 2.contact number, 3.description of activity.
                self.address = address_dict[self.choice]
                self.contactNumber = contactNumber_dict[self.choice]
                self.description = description_dict[self.choice]
                
                # Moves to step 6, Line .
                self._count+=1

            # To ensure that the user has typed casualeat
            elif msg['text'].lower()=='casualeat':


                # Create a c_restaurantkeyboard and c_restaurantmarkup which has the names of casual outlets for the user to select from.                   
                c_restaurantkeyboard=[]
                for c_restaurant_names in c_restaurant_names_list:
                    c_restaurantkeyboard.append([InlineKeyboardButton(text=c_restaurant_names, callback_data=c_restaurant_names)])
                global c_restaurantmarkup
                c_restaurantmarkup= InlineKeyboardMarkup(inline_keyboard=c_restaurantkeyboard)

                # Prints the names of casual outlets for users to choose from.
                self.sender.sendMessage('Here is a list of casual outlets to eat in Singapore! Please select one:', reply_markup=c_restaurantmarkup)
                self.sender.sendMessage('Please select the outlets provided')

                #Moves to step 6, Line .
                self._count+=1
                
            # If the user did not type go or casualeat, bot will execute these steps.
            else:

                if self.choice in activityname_list:
                    #Prints the message informing the user that he/she did not type go.
                    self.sender.sendMessage("You did not type go. Please select again.")
                    # time delay 1 second.
                    time.sleep(1)

                    #Prints the names of dating activities for the user to select from again.
                    self.sender.sendMessage('Here is a list of dating activities to do in Singapore for fun! Please select one:', reply_markup=activitymarkup)
                    self.sender.sendMessage('Please select the activity provided')

                    # Moves to step 4.
                    self._count-=1

                else:
                    #Prints the message informing the user that he/she did not type casualeat.
                    self.sender.sendMessage("You did not type casualeat. Please select again.")

                    # time delay 1 second.
                    time.sleep(1)

                    self.sender.sendMessage('Please select the type of eating option:', reply_markup=eating_choicekeyboard)

                    # Moves to step 4.
                    self._count-=1

        # Step 7: Show the information for the casual outlets selected by the user(Applicable for Eating only)
        elif self._count==6:

            # To check if the user typed 'casualeat'
            if msg['text'].lower()=='casualeat':
                # variable informationkeyboard is a list with information for the casual outlets such as 1. Address, 2. Description of Outlets, or 3. Try planning another date. 
                c_restaurantinformationkeyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Address', callback_data='1')],[InlineKeyboardButton(text='Description of Outlets', callback_data='2')],[InlineKeyboardButton(text='Try Planning Another Date', callback_data='3')]])
                self.sender.sendMessage('This is the list of information for the outlets you have chosen: \n',reply_markup=c_restaurantinformationkeyboard)
                self.sender.sendMessage('Please use the keyboard provided.')
                                           
                # Variables from line  to line  are assigned values based on 1.Address, 2.Description of Outlets.
                self.address = c_restaurant_address_dict[self.information]
                self.description = casual_description_dict[self.information]
                
                # Moves to step 8, Line .
                self._count+=1

            else:
                # Prints the message informing the user that he/she did not type casualeat.
                self.sender.sendMessage("You did not type casualeat. Please select again.")

                # time delay 1 second.
                time.sleep(1)

                # Prints the names of casual outlets for users to choose from again
                self.sender.sendMessage('Here is a list of casual outlets to eat in Singapore! Please select one:', reply_markup=c_restaurantmarkup)
                self.sender.sendMessage('Please select the outlets provided')

                # Moves to step 6.
                self._count-=1

bot = telepot.DelegatorBot("352062939:AAFyzUSKPERqEAjoDfagIR72vRdN38NXh1U", [
    include_callback_query_chat_id(pave_event_space())(
        per_chat_id(), create_open, MessageCounter, timeout=99500),
])

bot.message_loop(run_forever='Listening ...')


