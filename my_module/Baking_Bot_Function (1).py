import string

#collections of possible input and outputs
desserts_In =['tiramisu','cream','macarons','choco']
desserts_Out = ['Great! What do you want to know about?:']

user_choice = ['ingredient','tool', 'steps']

tiramisu_ing = ['4 eggs','130g of sugar','53g cake flour', '7g of cocoa powder', '3g instant coffee','45ml milk','25g unsalted butter','200g mascarpone cheese','100ml heavy cream','20ml hot water','2 gelatin sheets or 3g gelatin powder']
cream_ing = ['20g butter','30g water', '180ml milk', '40g flour', '3 egg', '1/2 vanilla bean or 1/2 teaspoon of vanilla extract', '150ml heavy cream']
macarons_ing = ['88g almond powder','88g powdered sugar', '110g egg whites','180g sugar','100ml milk','50ml heavy cream','1/2 vanilla bean or 1/2 teaspoon vanilla extract','20ml water','150g unsalted butter']
choco_ing = ['200g chocolate','50g double cream (at room temperature)','2 eggs(large)*beaten egg(room temperature)','10g cake flour']

tiramisu_steps = ['1) separate 2 egg yolk and whites, then whisk the whites while slowly adding 60g of sugar','2)once the whites become stiff add in two yolks','3)once the whites and yolk mixed well, add in the sifted cake flour and 7g of cocoa powder','4) Use a spatula to gently mix the flour and egg mixture *make sure you dont mix too much!*)', '5)Melt the butter into 25ml of milk and add a little bit of the cake mixture to the butter then mix', '6)Get the butter cake mixture and add it back into the cake mixture', '7) Pour out the cake batter onto a pan and bake in an oven preheat to 374 degree F for 11-13min','8)Melt the gelatin into 20ml of milk and mix 2 egg yolk with 20g of sugar','9)Mix the egg yolk mixture on top of hot water unitl it turn light yellow','10)add in the gelatin/milk mix into the egg yolk while its still warm','11)then get a spatula and add 200g mascarpone cheese to the egg yolk', '12)whip 100ml heavy cream with 10g sugar until its a little stiff and then add it into the cheese mixture','13)whisk 1 egg white with 10g sugar until its stiff and repeat the previous process','14)cut the cake into the shape of your cake pan','15)mix the hot water with instant coffee and 20g sugar','16)put the cake into the cake pan and soak it with the coffee syrup, then pour in the cheese mixture', '17) repeat step 16 until your cheese mixture is gone and refrigerate','18) take out the cake once the cheese mixture is harden and sift cocoa powder on top of the cake!', '19)Good Job! Its ready!' ]

cream_steps = ['1)heat up the milk with 1/2 teaspoon of vanilla extract/bean','2)whisk two egg yolk with 40g sugar and sift 15g flour into the bowl and mix', '3)Then add the milk you heated up earlier as you whisk','4)cook the mixture over medium-high heat whisking constantly so it doesnt burn *tip* use spatula', '5)once the cream becomes more solid-like, remove it from the heat and refrigerate','6)Sift 25g of flour and beat an egg in preparation', '7)heat up 30g water,30 milk, and 20g of butter in the same pan', '8)once the milk boils, add in the flour and mix with spatula','9)Continue mixing for about a minute and transfer it onto another bowl', '10)add in a little bit of the egg you beated earlier into the bowl and mix until you use up the egg','11)once the dough mixture has a nice consistency put it into a pipe and squeeze it out onto your baking sheet','12)bake it in 374 degree F for 20 min and then 338 degree F for 20-30 min', '13)Do not immediately the puff out of the oven and leave it there for a while after you turn off the oven','14)Once the oven cooled down take out the puff and leave it out, while you get the cream mixture', '15)mix the cream with a spatula until its smooth','16)whisk 150ml of heavy cream with 40g of sugar until its stiff','17) mix the heavy cream with the cream mixture and pour it into a piping bag','18)Use the piping bag and pour the cream into the puff','19)You finished! Enjoy!']

macarons_steps = ['1)Beat 70g egg whites and gradually add 60g of sugar 1/3 at a time','2)Beat until its stiff and sift 88g of almond powder and powdered sugar into the mixture','3)Use a spatula and gently fold the batter until everything just mixed *make sure you do not mix too much','4)Pour the mixtue into the piping bag','5)Spread out the parchment paper onto the pan and pipe the macarons onto the parchment','6)leave the macaron shell out for about an hour until its dry to the touch', '7)preheat the oven to 300 degree F and bake the macarons for 13-15 min','8) let the macarons cool down before you take it off of the parchment paper','9) while you wait for the macarons to cool make the milk jam', '10)pour 100ml milk, 50g sugar, and 50ml of heavy cream into a pan','11)use a spatula and stir it over low heat for 10 min until it become syrupy','12)let the milk jam cool before putting it into piping bag', '13)For buttercream, pour 70g sugar and 20ml water into a pot and cook it over low heat', '14)Beat the egg white while we wait for the sugar water to boil, *make sure the sugar doesnt burn!','15)once the sugar water or syrup becomes 244 degree F, gradually pour the syrup into the egg whites and conyinue to whisk it','16)Scrape the vanilla seeds or add 1/2 teaspoon of extract and add them in, continue to whisk','17)Make sure the meringue(the egg white) isnt too warm and add 150g of butter in 1/3 at a time','18)Transfer the buttercream into a piping bag','19)Pipe a swirl of buttercream around the edge of the macarons shell and fill the center with the milk jam','20)sandwich the shells together with the remaining halves and youre done!']

choco_steps = ['1)chop up the chocolate and put it into a bowl','2)Get a bigger bowl and pour hot water in(122 degree F)','3)Put the chocolate bowl on top of the hot water bowl and use a spatuala to mix the chocolate until it melts','4)Pour in 50g heavy cream into the melted chocolate and mix','5)Pour in the beaten egg into the chocolate bowl and mix again','6)take out the chocolate bowl out of the hot water and sift 10g of cake flour into the chocolate and mix well','7)Pour it into a cake pan lined with parchment paper(22x6)','8)Get a towel, place it underneath the pan and slam it down until you get rid of most bubbles in the cake mix', '9)Bake it in an oven preheated to 338 degree F for 17 min(be careful not to bake to much)','10) Take it out of the oven. Sift powdered sugar ontop of the cake and its ready to serve! Enjoy!']

tiramisu_tools =['spatula','hand mixer or whisk','at least 4 bowls or more','a cake pan', 'parchment paper','piping bag', 'sifter','*optional cooking thermometer','digital scale']
cream_tools =['spatula','hand mixer or whisk','at least 4 bowls or more','a cake pan', 'parchment paper','piping bag', 'sifter','*optional cooking thermometer','digital scale']
macarons_tools =['spatula','hand mixer or whisk','at least 4 bowls or more','a cake pan', 'parchment paper','piping bag', 'sifter','*optional cooking thermometer','digital scale']
choco_tools =['spatula','hand mixer or whisk','at least 4 bowls or more','a cake pan', 'parchment paper','piping bag', 'sifter','*optional cooking thermometer','digital scale']


def string_concatenator(string1, string2, separator):
    output = string1 + separator+ string2
    return output

def list_to_string(input_list, separator):
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output

def remove_punctuation(input_string):
    #This remove any punctuation from the user input
    out_string =''
    for x in input_string: 
        if x not in string.punctuation:
            out_string+=x
    return out_string

def prepare_text(input_list):
    """this method converts all strings into a lower case 
    and also removes punctuation
    
    input: string
    
    output: list
    """
    input_string = list_to_string(input_list,'')
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

def is_in_list(list_one, list_two):
    for element in list_two:
        if element in list_one:
            return True
    return False

#ends the chat
def end_chat (input_list):
    if 'bye' in input_list or 'quit' in input_list:
        return True
    else:
        return False

#Functions I created specifically for Baking Bot
def start():
    #initiates the conversation
    print('What kind of desserts do you want to make today?')
    print('(choose from this list: tiramisu, cream puff(just type cream), macarons, chocolate cake (just type choco)')
            
def is_Tiramisu(input_list):
    """checks if the input is 'tiramisu"""
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'tiramisu':
        return True
    else:
        return False
        
def is_Cream_Puff(input_list):   
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'cream':
        return True
    else:
        return False

def is_Macarons(input_list):     
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'macarons':
        return True
    else:
        return False
    
def is_Choco_Cake(input_list):
     
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'choco':
        return True
    else:
        return False 
    
def is_Ingredient(input_list):
     
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'ingredient':
        return True
    else:
        return False


def is_Tool(input_list):
     
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'tool':
        return True
    else:
        return False

def is_Steps(input_list):
     
    check = ''
    check = list_to_string(input_list,'' )
    if check.lower() == 'steps':
        return True
    else:
        return False

def lets_talk():
    """Main function to run the bot"""
    chat = True
    outs = []
    print('Mochi: Hi,Im Mochi! Welcome to Baking Advice!')

    #Checks that the conversation is still ongoing
    while chat:
        start()
        #Gets the users input
        msg = input('You :\t')
        out_msg = None
        msg = prepare_text(msg)
        
        #Check if input is 'tiramisu'
        tiramisu = is_Tiramisu(msg)
        
        #Checks if input is 'cream puff'
        cream_puff = is_Cream_Puff(msg)
        
        #Checks if input is 'macarons'
        macarons = is_Macarons(msg)
        
        #Checks if input is 'choco cake'
        choco_cake = is_Choco_Cake(msg)
        
        #Checks if input is 'ingredient
        ingredient = is_Ingredient(msg)
        
        #Checks if input is 'tool'
        tool = is_Tool(msg)
        
        #Checks if input is 'steps'
        steps = is_Steps(msg)
        
        msg = prepare_text(msg)
        
        if end_chat(msg):
            out_msg = ['Sayonara~ ꒰๑•௰•๑꒱♫']
            chat = False
            
        if not out_msg:
            
            #if the input is one of the dessert choices I provided it runs
                
            if is_in_list(msg, desserts_In):
                out_msg = 'Great! What do you want to know about?:' + 'ingredient','tool', 'steps to make it (just type steps)'
                print(out_msg)
                msg = input('You :\t')
                if tiramisu:
                    #If the user puts in an input not in the list provided it will return the out_msg
                    if not is_in_list(msg,user_choice):
                        out_msg = ['follow the direction! ꒰｀꒳´꒱', 'Choose from: ingredient, tool, steps to make it (just type steps)']
                    #If the user puts in an input from the list provided it will continue
                    elif is_in_list(msg,user_choice):
                        if is_Tool(msg):
                            out_msg = tiramisu_tools
                        elif is_Ingredient(msg):
                            out_msg = tiramisu_ing
                        elif is_Steps(msg):
                            out_msg = tiramisu_steps
                        
                elif cream_puff:
                    #If the user puts in an input not in the list provided it will return the out_msg
                    if not is_in_list(msg,user_choice):
                        out_msg = ['follow the direction! ꒰｀꒳´꒱', 'Choose from: ingredient, tool, steps to make it (just type steps)']
                    #If the user puts in an input from the list provided it will continue
                    elif is_in_list(msg,user_choice):
                        if is_Tool(msg):
                            out_msg = cream_tools
                        elif is_Ingredient(msg):
                            out_msg = cream_ing
                        elif is_Steps(msg):
                            out_msg = cream_steps
                
                elif macarons:
                    #If the user puts in an input not in the list provided it will return the out_msg
                    if not is_in_list(msg,user_choice):
                        out_msg = ['follow the direction! ꒰｀꒳´꒱', 'Choose from: ingredient, tool, steps to make it (just type steps)']
             
                    #If the user puts in an input from the list provided it will continue
                    elif is_in_list(msg, user_choice):
                        if is_Tool(msg):
                            out_msg = macarons_tools
                        elif is_Ingredient(msg):
                            out_msg = macarons_ing
                        elif is_Steps(msg):
                            out_msg = macarons_steps
                           
                elif choco_cake == True:
                    #If the user puts in an input not in the list provided it will return the out_msg
                    if not is_in_list(msg,user_choice):
                        out_msg = ['follow the direction! ꒰｀꒳´꒱', 'Choose from: ingredient, tool, steps to make it (just type steps)']
             
                    #If the user puts in an input from the list provided it will continue
                    elif is_in_list(msg, user_choice):
                        if is_Tool(msg):
                            out_msg = choco_tools
                        elif is_Ingredient(msg):
                            out_msg = choco_ing
                        elif is_Steps(msg):
                            out_msg = choco_steps

            else:
                out_msg = ['Hmm sorry I dont understand ꒰•̤▿•̤*ૢ꒱???... please choose from the list I provided!'+"(tiramisu,cream puff,macarons,choco cake)"]
            
            
        #prints response to user
        print('Mochi: ')
        for x in out_msg:
            print("    " + x)
                    
