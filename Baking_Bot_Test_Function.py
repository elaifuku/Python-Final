"""It's a test for Baking_Bot_Functions. It is used to test most of the functions in the program. 
"""

from my_module.Baking_Bot_Function.py import *

##test variables
test_string = 'hello, People'
test_list = ['hello,','People']

def string_concatenator():
    """Tests string_concatenator function"""
    assert string_concatenator('hello','People',',') == test_string 
    assert isinstance(string_concatenator('hello','People',','),str)
    assert callable(string_concatenator)
    
def list_to_string():
    """Tests list_string_concatenator function"""
    assert list_to_string(test_list, ' ' == test_string)
    assert isinstance(list_to_string(['hello','People']',')
    assert callable(list_to_string)
                  
def remove_punctuation():
    """Tests remove_punctuation function""" 
    assert callable(remove_punctuation)
    assert isinstance(remove_punctuation('a'),str)
    assert remove_punctuation("Hi! I'm Mochi!") == "Hi I'm Mochi"                      
                     
def test_prepare_text():
    """Tests prepare_text"""
    assert ['hello,People'] == prepare_text(test_string)  
    assert isinstance(prepare_text(test_string),list)
    assert callable(prepare_text)  
                      
def test_is_in_list(list_one, list_two):
    """Tests is_in_list function"""
    assert is_in_list(['a','b'],['a','b','c','d']) == True
    assert isinstance(is_in_list(['a','b'],['a','b','c','d']),bool)
    assert callable(is_in_list)
    
def test_end_chat():
    """Tests end_chat function"""
    assert end_chat(test_list) == False
    assert isinstance(end_chat(test_list),bool)
    assert callable(end_chat)
              
def test_is_Tiramisu():
    """Tests is_Tiramisu function"""
    assert is_Tiramisu(['tiramisu']) == True                  
    assert isinstance(is_Tiramisu(['tiramisu']),bool)   
    assert callable(is_Tiramisu)                  
                      
def test_is_Cream_Puff():
    """Test is_Cream_Puff function"""
    assert is_Cream_Puff(['cream puff']) == True                  
    assert isinstance(is_Cream_Puff(['cream puff']),bool)
    assert callable(is_Cream_Puff)
                      
def test_is_Macarons():
    """Tests is_Macarons function"""
    assert is_Tiramisu(['macarons']) == True                  
    assert isinstance(is_Macarons(['macarons']),bool)   
    assert callable(is_Macarons)                              
                      
def test_is_Choco_Cake():
    """Tests is_Choco_Cake function"""
    assert is_Tiramisu(['choco cake']) == True                  
    assert isinstance(is_Choco_Cake(['choco cake']),bool)   
    assert callable(is_Choco_Cake)                              
                      
def test_is_Ingredient(): 
    """Tests is_Ingredient functions"""                  
    assert is_Ingredient(['ingredient']) == True
    assert isinstance(is_Ingredient(['ingredient']),bool)
    assert callable(is_Ingredient)                  
                      
def test_is_Tool():
     """Tests is_Tool functions"""                 
     assert is_Tool(['tool']) == True                 
     assert isinstance(is_Tool(['tool']),bool)
     assert callable(is_Tool)   
                      
def test_is_Steps():
    """Tests is_Steps functions"""                  
    assert is_Steps(['steps']) == True                  
    assert isinstance(is_Steps(['steps']),bool)                  
    assert callable(is_Steps)
                      
def test_get_TiramisuI():
    """Tests get_TiramisuI function"""
    assert get_TiramisuI(['ingredient']) == tiramisu_ing                  
    assert isinstance(get_TiramisuI(['ingredient']),list)                   
    assert callable(get_TiramisuI)
                      
def test_get_Cream_PuffI():
    """Tests get_Cream_PuffI function"""
    assert get_Cream_PuffI(['ingredient']) == cream_ing                  
    assert isinstance(get_Cream_PuffI(['ingredient']),list)                 
    assert callable(get_Cream_PuffI)

def test_get_MacaronsI():
    """Tests get_MacaronsI function"""
    assert get_MacaronsI(['ingredient']) == macarons_ing                  
    assert isinstance(get_MacaronsI(['ingredient']),list)                   
    assert callable(get_MacaronsI)

def test_get_ChocoI():
    """Tests get_ChocoI function"""
    assert get_ChocoI(['ingredient']) == choco_ing                  
    assert isinstance(get_ChocoI(['ingredient']),list)                   
    assert callable(get_ChocoI)

def test_get_TiramisuS():
    """Tests get_TiramisuS function"""
    assert get_TiramisuS(['steps']) == tiramisu_steps                  
    assert isinstance(get_TiramisuS(['steps']),list)                   
    assert callable(get_TiramisuS)

def test_get_Cream_PuffS():
    """Tests get_Cream_PuffS function"""
    assert get_Cream_PuffS(['steps']) == cream_steps                  
    assert isinstance(get_Cream_PuffS(['steps']),list)  
    assert callable(get_Cream_PuffS)

def test_get_MacaronsS():
    """Tests get_MacaronsS function"""
    assert get_MacaronsS(['steps']) == macarons_steps                  
    assert isinstance(get_MacaronsS(['steps']),list)                   
    assert callable(get_MacaronsS)

def test_get_ChocoS():
    """Tests get_ChocoS function"""
    assert get_ChocoS(['steps']) == choco_steps                  
    assert isinstance(get_ChocoS(['steps']),list)                   
    assert callable(get_ChocoS)
                      
                      
def test_everything():
   """I borrowed this idea from Byungwon's League_Bot This function test all the test function at once"""
    string_concatenator():
    list_to_string():
    remove_punctuation():
    test_prepare_text():
    test_is_in_list(list_one, list_two):
    test_end_chat():
    test_is_Tiramisu():
    test_is_Cream_Puff():
    test_is_Macarons():
    test_is_Choco_Cake():
    test_is_Ingredient(): 
    test_is_Tool():
    test_is_Steps():
    test_get_TiramisuI():
    test_get_Cream_PuffI():
    test_get_MacaronsI():
    test_get_ChocoI():
    test_get_TiramisuS():
    test_get_Cream_PuffS():
    test_get_MacaronsS():
    test_get_ChocoS():
    