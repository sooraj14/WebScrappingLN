from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#linkedim username and password stored in info.py file
from info import email, pas
#we can use chrome or any other web application
disk = webdriver.Firefox()

states = ['new delhi', 'Maharastra', 'Karnataka', 'Harayana', 'goa']

#opening the career website I used this function
def Career():
    count = 0
    des = []   #des is the list that stores the job data     
    disk.get("https://www.careerguide.com/career-options")  #this link is to open the URL
    sleep(3)
    details = disk.find_element(
        By.XPATH, '/html/body/form/div[6]/div[3]/div/div[2]').text #path of the des #.text converts the path details to text form
    details = details.splitlines() # to remove /n

    for x in details:
        des.append(x)
        count += 1
        if count == 5:
            break
    print(des)
    return des

#This is about linkedin page
def Linkedin(disc):     
    disk.get("https://www.linkedin.com/login") #to open the linkedin URL
    disk.implicitly_wait(5) # to  load the page
    sleep(3)
    login_block = disk.find_element(By.ID, 'username') # path of username is located
    login_block.send_keys(email)
    password_block = disk.find_element(By.ID, 'password') # path of password is located
    password_block.send_keys(pas)
    password_block.send_keys(Keys.ENTER) # ENTER is the keyword to press the enter button
    sleep(2)
    
# the above loops are to search the jobs in the disc list
    for i in range(len(disc)):
        about_jobs = []        
        link = []       
        company = []               
        print(f"\t{disc[i]} details -->")
        sleep(4)
    #the below link is seaching the URL to open job disc and states
        disk.get('https://www.linkedin.com/jobs/search/?currentJobId=3350373647&keywords={a}&location={b}%2C%20India&refresh=true'.format(
            a=disc[i], b=states[i]))      

        sleep(2)

        ul_body = disk.find_element(
            By.CLASS_NAME, 'scaffold-layout__list-container') # here I used classname instead of path

        docs = ul_body.find_elements(By.TAG_NAME, 'li')
    #seaching all the list tags for the data present in the jobs
        for doc in docs:
            text = doc.text
            if len(text) > 4:
                about_jobs.append(text)
        print(f"\tJob details for {disc[i]}-->\t {about_jobs}")

        docs = ul_body.find_elements(By.TAG_NAME, 'a')
    #searching all the a tag which the link  is associated 
        for doc in docs:
            all_links = doc.get_attribute('href')
            if ".com/company/" in all_links:
                company.append(all_links)
            elif ".com/jobs/view/" in all_links:
                if all_links not in link:
                    link.append(all_links)
        print(f"\tThe Link For The Application for {disc[i]}\t {link}")
        print(f"\tCompany linkedin Page Link--> {company}\t")
        print(f"\tThe company Details Link For {disc[i]}\t")

        for i in range(len(company)):
            About_dict = {}
            disk.get(company[i].format('about/'))
            sleep(2)

            try:  # checks the about button,if about button is exists then it goes for another page or else it checks in same page.
                button = disk.find_element(
                    By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[1]/section/footer')
                button.click()
            except:
                try:
                    detail_in = disk.find_element(
                        By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/p').text

                    About_dict['description'] = detail_in
                except:
                    About_dict['description'] = "None"


                try:# searching for the no. of employee working for them
                    Employee_box = disk.find_element(
                        By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[3]').text

                    About_dict['no Employees'] = Employee_box
                except:
                    About_dict['no Employees'] = "None"

                try:  # searching for the headquater location
                    Comp_Location = disk.find_element(
                        By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[5]').text

                    About_dict["headquater"] = Comp_Location
                except:
                    About_dict['headquater'] = "None"

                print(f'The Company Details --->{About_dict}')
                continue


            try: # searching for the description details of the company
                detail_in = disk.find_element(
                    By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/p').text
                detail_in.splitlines()
                About_dict['description'] = detail_in
            except:
                About_dict['description'] = "None"

            try:# searching for the no. of employee
                Employee_box = disk.find_element(
                    By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[3]').text

                About_dict['no Employees'] = Employee_box
            except:
                About_dict['no Employees'] = "None"

            try:  
                Comp_Location = disk.find_element(
                    By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[5]').text

                About_dict["headquater"] = Comp_Location
            except:
                About_dict['headquater'] = "None"

            print(f'The Company Details --->{About_dict}')

            print("\n")

# to separate it from the other python modules
if __name__ == '__main__':
    lst = Career()
    Linkedin(lst)
    disk.close()
