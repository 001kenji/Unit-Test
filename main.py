import unittest,json,re,datetime,time
#from password_generator import PasswordGenerator
from password_generator import PasswordGenerator
import timeout_decorator
IdietLevel = int()
number = re.compile(r'^[0-9\s]*$')

def Redirect(props):
    if(props == 'Welcome'):
        Welcome('Rerun')
    elif(props == 'SurfApplication'):
        SurfApplication('RerunIdiet')


def Fool(props):
    global IdietLevel
    IdietLevel += 1
    print('------------------------------------------------------')
    sentense = 'What a fool😒.Follow the instructions provided. \nError: {}'
    print(sentense.format(props))
    return

def SpesifiedChoices(props):
    with open('./short.json','r') as DBItem:
        dump = DBItem.read()
        data = json.loads(dump)
        list = []        
        for dt in range(0,len(data)):
        
            name = str(data[dt]['itemType'])
            if(name.lower() == props):
                list.append(data[dt])
    DBItem.close()
    #----------------for exception raise error unittest perpose
    # if(len(list) == 0):
    #     raise Exception('There is no value found')
    return list

def CreateDoc(data,name):
    val = '{}.json'
    with open(val.format(name),'x') as NewFile:
        NewFile.write(data)        
        NewFile.close()
    return

def OverviewChoices():
    with open('./short.json','r') as DBItem:
        dump = DBItem.read()
        data = json.loads(dump)
        list = []
        
        for dt in range(0,len(data)):
            for x,y in data[dt].items():
                if(x == 'itemType' and y not in list):
                    list.append(y)
    DBItem.close()
    return list



def SurfApplication(props):
    if(props == 'Normal'):
        print('\nThe following are the items we possess for the moment.\nPlese study the list bellow then type your choice down.\n')
    elif (props == 'RerunIdiet'):
        sentense = 'Your now level {} fool...'
        global IdietLevel
        print(sentense.format(IdietLevel))
        print('\nLets make things easy for us, once again dont be a fool 🧐.\nPlese study the list bellow then type your choice down.\n')
    
    data = OverviewChoices()
    sentense = ''
    for x in data:
        val = ' {},'
        valP = val.format(x)
        sentense += valP
    print(sentense)
    choice = input('\nEnter your choice: ')
    result = SpesifiedChoices(choice.lower())
    if(len(result) == 0):
        Fool('Invalid choice')
        Redirect('SurfApplication')
        return
   

    for dt in range(0,len(result)):
        num = dt
        
        name = result[dt]['name']
        price = result[dt]['price']
        description = result[dt]['description']
        itemType = result[dt]['itemType']
        sentense = '\nNumber : {0}\nNAME : {1}\nPRICE : {2}\nDESCRIPTION : {3}\nITEMTYPE : {4}'
        print(sentense.format(num,name,price,description,itemType))
    print('\nThis are the items available for your choice.\nIdentify the disired item them type down its "Number".')
    choice = input('\nEnter number: ')
    if not number.match(choice):
        Fool('Input is not a number')
        Redirect('SurfApplication')
        return
    name = input('\nEnter a name that will be used to create a file containing the selected item: ')
    data = json.dumps(result[int(choice)],indent=4)
    if(len(name) == 0):
        Fool('Oooh shiet😱.You\'ve come this far to fail.')
        name = input('\nEnter a name that will be used to create a file containing the selected item: ')
        if(len(name) == 0):
            sentense = 'Go home.And for your information your a level {} fool.'
            print(sentense.format(IdietLevel))
            return 0
    CreateDoc(data=data,name=name)

    finaly = '\n\n\n(❁´◡`❁) (❁´◡`❁) (❁´◡`❁) (❁´◡`❁)\nAll rights reserved © {0}. Art designed by Brian Njuguna \n(❁´◡`❁) (❁´◡`❁) (❁´◡`❁) (❁´◡`❁)\n\n\n'
    year = datetime.datetime.now().year

    finalyFormated = finaly.format(year)
    print(finalyFormated)
    return



def Welcome(props):
    if(props != 'Rerun'):
        print('\nWelcome to B-Intel E-commerce application.😁')

    SurfApplication('Normal')
        

Welcome('')
DoneTest = 0
class MainTest(unittest.TestCase):
   
    def setUp(self) -> None:
        print('\n--------------Starting test--------------\n')
        
        return super().setUp()


    def tearDown(self) -> None:
        global DoneTest
        DoneTest += 1
        
        sentense = '\n--------------Done Test {0}--------------\n'
        
        print(sentense.format(DoneTest))
        return super().tearDown()

    def test_Item(self):
        val = SpesifiedChoices('mug')
        self.assertIs(type(val),list,'Result is not a list')
        #----------------for exception raise error unittest perpose
        #self.assertRaises(Exception,SpesifiedChoices,'mas')

    def test_Choices(self):
        val = OverviewChoices()
        self.assertIs(type(val),list,'Result is not a list')
        self.assertIn('mug',val,'value not found')

    #@timeout_decorator.timeout(5)
    def test_timetest(self):
        password = PasswordGenerator()
        #password.minlen = 10
        i = 0
        print('Minimum time to generate password: 5 sec')
        for i in range(0,11,1):
            time.sleep(1)
            x = 10 - i
            print('Generating password in: ',x)
            if i == 10:
                myPassword = password.generate()
        print("New generated password: ",myPassword,"\n Time taken to generate: ",i,"sec")

        # Check if the password was generated within the time limit
        if i > 5:
            self.fail("Password generation took too long: {} seconds".format(i))

    @unittest.skip('This is just a foolish test')
    def test_Demo(self):
        val = OverviewChoices()
        self.assertIsNot(type(val),dict,'This is not a dictionary')

    

 
        
if __name__ == '__main__':
    unittest.main()
    runner = unittest.TextTestResult()
    class1 = MainTest()
    runner.testsRun(class1)
