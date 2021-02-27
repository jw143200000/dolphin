from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time

class mProAutomate:

    # Axis - 655393 | india@2020
    # YBL  - 718842 | mnyl@4321 | Customer ID-  29471, 47942, 616658, 626018, 866238 (222222), 2454, 2455, 2456, 2457
    # DST  - 934384 | MNYL@2020
    # SPARC- 782058 | MNYL@2020
    # Agency- 447660, 127065| Mnyl@2020
    #Ingenium- http://ing247test.maxlifeinsurance.com/ingenium/servlet/pageserver?ProcessClassID=SignOn&PageReturn=index&LocaleID=E



    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://sitminte.maxlifeinsurance.com/mSalesTest/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5000)
        self.wait = WebDriverWait(self.driver, 5000)
        action = AC(self.driver)

    def loginFunctionality(self):

        agentID= self.driver.find_element(By.ID, "agent_id")
        agentID.clear()
        agentID.send_keys("654796")

        crmID = self.driver.find_element(By.ID, "crm_id")
        crmID.clear()
        crmID.send_keys("1000057412")

        custID= self.driver.find_element(By.ID, "customer_id")
        custID.clear()
        custID.send_keys("956271260")

        btnProccedTomSales=self.driver.find_element(By.XPATH,"//*[contains(text(),'Proceed')]")
        btnProccedTomSales.click()
        print("Proceeded To mSALES.")
        time.sleep(8)
        windowBefore = self.driver.window_handles
        print(windowBefore)
        self.driver.switch_to.window(windowBefore[1])

        countryDropdown= self.driver.find_element(By.XPATH, "(//*[@placeholder= 'COUNTRY'])[1]")
        countryDropdown.click()
        time.sleep(1)
        selectIndia = self.driver.find_element(By.XPATH, "(//*[contains(text(),'India')])[1]")
        selectIndia.click()
        time.sleep(2)

        btnAdd= self.driver.find_element(By.XPATH, "//*[@class='addThisText']")
        btnAdd.click()
        print("Lead added")
        time.sleep(5)

        insuredLifeDropdown = self.driver.find_element(By.XPATH, "(//select)[1]")
        insuredLifeDropdown.click()
        time.sleep(1)

        yesinsuredLifeDropdown= self.driver.find_element(By.XPATH, "//*[contains(text(),'Yes')]")
        yesinsuredLifeDropdown.click()
        time.sleep(1)

        selectIncomeDropdown = self.driver.find_element(By.XPATH, "(//select)[2]")
        selectIncomeDropdown.click()
        time.sleep(1)
        optionselectIncomeDropdown= self.driver.find_element(By.XPATH, "//*[contains(text(),'5 to 10 lakhs pa')]")
        optionselectIncomeDropdown.click()
        time.sleep(1)

        selectEducationDropdown = self.driver.find_element(By.XPATH, "(//select)[4]")
        selectEducationDropdown.click()
        time.sleep(1)
        optionInselectEducationDropdown = self.driver.find_element(By.XPATH, "//*[contains(text(),'Professional')]")
        optionInselectEducationDropdown.click()
        time.sleep(1)

    def selectPlan(self):

        categorySelect= self.driver.find_element(By.XPATH, "//*[contains(text(),'CLOSE TO RETIREMENT OR RETIRED')]")
        categorySelect.click()
        print("Plan Selected")

        planSelect = self.driver.find_element(By.XPATH, "//*[contains(text(),'PROTECTION')]")
        planSelect.click()
        time.sleep(1)

        clickonProductRecommendation = self.driver.find_element(By.XPATH, "//*[@value='PRODUCT RECOMMENDATION']")
        clickonProductRecommendation.click()
        print("Button clicked")
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Max Life Saral Jeevan Bima')]")))
        optionInPlan= self.driver.find_element(By.XPATH, "//*[contains(text(),'Max Life Saral Jeevan Bima')]")
        optionInPlan.click()
        time.sleep(3)

        clickonProceed = self.driver.find_element(By.XPATH, "//*[@value='PROCEED']")
        clickonProceed.click()
        print("Proceed Button clicked")
        time.sleep(8)


    def goalCalculator(self):

        paymentPeriodDropdown = self.driver.find_element(By.XPATH, "(//select)[2]")
        paymentPeriodDropdown.click()
        time.sleep(1)
        optionInselectEducationDropdown = self.driver.find_element(By.XPATH, "(//*[@value='18'])[2]")
        optionInselectEducationDropdown.click()
        time.sleep(1)

        lumpsumpSavings = self.driver.find_element(By.XPATH, "(//*[@type='number'])[3]")
        lumpsumpSavings.send_keys("300000")
        time.sleep(1)

        recurringSavings = self.driver.find_element(By.XPATH, "(//*[@type='number'])[4]")
        recurringSavings.send_keys("300000")
        time.sleep(1)

        premiumCommitment = self.driver.find_element(By.XPATH, "(//*[@type='number'])[7]")
        premiumCommitment.clear()
        premiumCommitment.send_keys("300000")
        time.sleep(1)

        buttonCalculate = self.driver.find_element(By.XPATH, "//*[contains(text(),'Calculate')]")
        buttonCalculate.click()
        time.sleep(1)

        clickonProceed = self.driver.find_element(By.XPATH, "//*[@value='Proceed']")
        clickonProceed.click()
        print("Proceed Button clicked")
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='NO']")))
        buttonNoClick = self.driver.find_element(By.XPATH, "//*[@value='NO']")
        buttonNoClick.click()
        time.sleep(1)

    def illustration(self):

        self.wait.until(EC.element_to_be_clickable((By.ID, "nationality")))
        nationalityDropdown = self.driver.find_element(By.ID,"nationality")
        nationalityDropdown.click()
        time.sleep(1)
        selectIndian = self.driver.find_element(By.XPATH,"//*[contains(text(), 'Indian')]")
        selectIndian.click()
        time.sleep(1)
        print("Indian Selected. Please select Riders first and then enter Mobile number.")

        alternateNumber = self.driver.find_element(By.NAME, "mobile2")
        alternateNumber.send_keys("9650479781")
        time.sleep(1)
        print("Alternate Number entered.")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='9650479781']")))
        print("Alternate mobile number Enterd.")

        premiumPaymentTerm = self.driver.find_element(By.ID, "ppt")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInpremiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[contains(text(),'10')])[1]")
        optionInpremiumPaymentTerm.click()
        time.sleep(1)
        print("Limited Pay Selected")
        time.sleep(1)


        premiumPaymentType = self.driver.find_element(By.ID, "premiumPaymentType")
        premiumPaymentType.click()
        time.sleep(1)
        optionInpremiumPaymentType = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Limited Pay')])[1]")
        optionInpremiumPaymentType.click()
        time.sleep(1)
        print("Limited Pay Selected")
        time.sleep(1)

        PolicyTerm = self.driver.find_element(By.ID, "policyTerm")
        PolicyTerm.click()
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "(//*[contains(text(),'15')])[1]")
        optionInPolicyTerm.click()
        time.sleep(1)
        print("Policy Term Selected")
        time.sleep(1)

        premiumPaymentMode = self.driver.find_element(By.ID, "premiumPayingMode")
        premiumPaymentMode.click()
        time.sleep(1)
        optionInpremiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Annually')])[1]")
        optionInpremiumPaymentTerm.click()
        time.sleep(1)
        print("Mode Selected")
        time.sleep(1)

        annualIncome = self.driver.find_element(By.ID, "annualIncome")
        annualIncome.send_keys("600000")
        annualIncome.clear()
        time.sleep(1)
        annualIncome.send_keys("600000")
        print("Annual Income Filled")

        sumAssured = self.driver.find_element(By.ID, "sumAssured")
        sumAssured.send_keys("600000")
        time.sleep(1)
        sumAssured.clear()
        sumAssured.send_keys("600000")
        time.sleep(1)
        print("sumAssured Filled")

        # buttonGetQuote = self.driver.find_element(By.XPATH, "//*[@value='Get Quote ']")
        # buttonGetQuote.click()
        # print("Quote Button Clicked")
        # time.sleep(5)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='Generate Illustration']")))
        buttonGenerateIll = self.driver.find_element(By.XPATH, "//*[@value='Generate Illustration']")
        buttonGenerateIll.click()
        time.sleep(5)
        print("Illustration Generated")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@type='checkbox']")))
        tickCheckbox = self.driver.find_element(By.XPATH, "//*[@type='checkbox']")
        tickCheckbox.click()
        time.sleep(1)
        print("Terms and Conditions Selected")

        buttonEmail = self.driver.find_element(By.XPATH, "//*[@value='EMAIL']")
        buttonEmail.click()
        time.sleep(2)

        buttonsEND = self.driver.find_element(By.XPATH, "//*[@value='SEND']")
        buttonsEND.click()
        time.sleep(2)
        print("Illustration sent")

        buttonProceed = self.driver.find_element(By.XPATH, "//*[@value='PROCEED']")
        buttonProceed.click()
        time.sleep(4)
        print("Proceed Clicked After Illustration")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='account']")))
        buttonAccount = self.driver.find_element(By.XPATH, "//*[@name='account']")
        buttonAccount.click()
        time.sleep(2)
        print("Account Clicked")
        print("HERE CLICK ON THE CONSENT LINK. Click on the Consent Link")
        time.sleep(30)
        buttonSubmit = self.driver.find_element(By.XPATH, "//*[contains(text(), 'SUBMIT')]")
        buttonSubmit.click()
        time.sleep(1)
        print("Submit button clicked")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Thank')]")))

        time.sleep(10)

        windowBefore = self.driver.window_handles
        print(windowBefore)

        ######## Switch to mPRO########
        self.driver.switch_to.window(windowBefore[2])

        self.wait.until(EC.element_to_be_clickable((By.ID, "userId")))

        username = self.driver.find_element(By.ID, "userId")
        username.send_keys("654796")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("india@2020")

        btnSign = self.driver.find_element(By.XPATH, "//*[contains(text(),'SIGN')]")
        btnSign.click()
        print("Switched to mPRO. Please click on Transaction.")



    def mPROStepOne(self):


        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='rs1']")))
        time.sleep(5)
        radioButtonSelf = self.driver.find_element(By.XPATH, "//*[@for='i2']")
        radioButtonSelf.click()
        time.sleep(1)
        print("Self Clicked")

        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()

        time.sleep(3)

    def mPROStepTwo(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='permanentHouseNo']")))

        houseNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentHouseNo']")
        houseNumberFill.clear()
        houseNumberFill.send_keys('12312')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentRoadNo']")
        roadNumberFill.clear()
        roadNumberFill.send_keys('12312')

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCountry']")
        countryFill.send_keys('India')
        time.sleep(1)
        countryFill.clear()
        time.sleep(1)
        countryFill.send_keys('India')
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Ind')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='permanentState']")
        stateFill.clear()
        stateFill.send_keys('MAHA')
        time.sleep(1)
        stateToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'MAHA')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.clear()
        cityFill.send_keys('MUM')
        time.sleep(1)
        cityToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'MUM')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill = self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.clear()
        pinToFill.send_keys('400081')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateNumberToFill.clear()
        alternateNumberToFill.send_keys('7977412402')
        print("Alternate number Filled")
        time.sleep(1)

        proofDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        proofDropdown.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='liId_Voter ID']")))
        proofSel = self.driver.find_element(By.XPATH, "//*[@id='liId_Voter ID']")
        proofSel.click()
        time.sleep(1)

        proofDropdownSecond = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        proofDropdownSecond.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='liId_Voter ID']")))
        proofSel = self.driver.find_element(By.XPATH, "//*[@id='liId_Voter ID']")
        proofSel.click()
        time.sleep(1)
        addProofEnter = self.driver.find_element(By.XPATH, "//*[@name= 'proofNumber']")
        addProofEnter.send_keys("123456789012")
        time.sleep(1)

        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()
        time.sleep(10)

        windowBefore = self.driver.window_handles
        print(windowBefore)

        self.driver.switch_to.window(windowBefore[2])

    def mPROStepThree(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        time.sleep(1)
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Father")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Mother")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Married Selected")
        time.sleep(2)

        # annualIncome = self.driver.find_element(By.XPATH, "//*[@name='income']")
        # annualIncome.clear()
        # time.sleep(1)
        # annualIncome.send_keys("500000")
        # time.sleep(1)

        industrySelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Mining']")
        optionInIndustrySelect.click()
        print("Industry Selected")
        time.sleep(1)

        orgCategory = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        orgCategory.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Partner/Prop']")
        optionInIndustrySelect.click()
        print("Organization Selected")
        time.sleep(1)

        occupation = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        occupation.click()
        time.sleep(1)
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Professional']")
        optionInOccupation.click()
        print("Occupation Selected")
        time.sleep(1)

        # organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        # organisationFill.send_keys("ORG")

        preferredLanguage = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[7]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Kannada']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        nomineeName = self.driver.find_element(By.XPATH, "//*[@name='nomineeName']")
        nomineeName.send_keys("Nominee")
        time.sleep(1)

        calNominee = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        calNominee.click()
        time.sleep(1)


        yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearNomineeSel = Select(yearNomineeDropdown)
        yearNomineeSel.select_by_value('1991')

        monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthNomineeSel = Select(monthNomineeDropdown)
        monthNomineeSel.select_by_value('0')

        dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-29']")
        dateNomineeSel.click()

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Male')]")
        genderSelected.click()
        print("Gender Clicked")

        relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[9]")
        relationshipProposer.click()
        time.sleep(1)
        optionInRelationshipProposer= self.driver.find_element(By.XPATH, "//*[@id ='liId_Brother']")
        optionInRelationshipProposer.click()
        print("Relationship Brother Selected.")
        time.sleep(1)

        # childName = self.driver.find_element(By.XPATH, "//*[@name='nomineeChildName']")
        # childName.send_keys("Chintu Kumar")
        # time.sleep(1)
        # childcalendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeChildDob']")
        # childcalendarNomineeFill.click()
        # time.sleep(1)
        #
        # childyearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        # childyearNomineeSel = Select(childyearNomineeDropdown)
        # childyearNomineeSel.select_by_value('2011')
        #
        # childmonthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        # childmonthNomineeSel = Select(childmonthNomineeDropdown)
        # childmonthNomineeSel.select_by_value('11')
        #
        # childdateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-22']")
        # childdateNomineeSel.click()
        # time.sleep(1)

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("411211012")
        time.sleep(3)

        # fetchVoucher = self.driver.find_element(By.XPATH, "//*[contains(text(),'Fetch Voucher Number')]")
        # fetchVoucher.click()
        #
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='MAXCRM4825852887226709999']")))
        #
        # time.sleep(5)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Proceed')]")))
        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()
        time.sleep(5)

    def mPROStepFour(self):

        hazardousActivitiesSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[6]")
        hazardousActivitiesSelect.click()

        criminalSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[7]")
        criminalSelect.click()

        travelSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[8]")
        travelSelect.click()

        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[4]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[5]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='weight']")
        weightFill.click()
        weightFill.send_keys("76")
        time.sleep(2)

        sugarSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[9]")
        sugarSelect.click()
        tensionSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[10]")
        tensionSelect.click()
        heartSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[11]")
        heartSelect.click()
        breathingSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[12]")
        breathingSelect.click()
        liverSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[13]")
        liverSelect.click()
        abnormalSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[14]")
        abnormalSelect.click()
        kidneySelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[15]")
        kidneySelect.click()
        mentalSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[16]")
        mentalSelect.click()
        jointSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[17]")
        jointSelect.click()
        historySelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[18]")
        historySelect.click()
        adviseSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[19]")
        adviseSelect.click()
        diagonseSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[20]")
        diagonseSelect.click()
        familySelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[21]")
        familySelect.click()
        tobaccoSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[22]")
        tobaccoSelect.click()
        alcoholSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[23]")
        alcoholSelect.click()
        drugsSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[24]")
        drugsSelect.click()

        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Cancel')]")))

        # clickCancel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Cancel')]")
        # clickCancel.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popupProceed']")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")

    def mPROStepFive(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Documents')]")))
        paymentStep5= self.driver.find_element(By.XPATH, "//*[contains(text(),'Documents')]")
        paymentStep5.click()

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='Cheque']")))
        # radioCheque = self.driver.find_element(By.XPATH, "//*[@for='Cheque']")
        # radioCheque.click()
        # print("Cheque Selected.")
        #
        # chequeFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeNumber']")
        # chequeFill.send_keys('1234567234')
        #
        # calendarSelect = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeDate']")
        # calendarSelect.click()
        # time.sleep(1)
        # chequeDateSelect = self.driver.find_element(By.XPATH, "//*[text()='2']")
        # chequeDateSelect.click()
        #
        #
        # chequePayableSelect= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[2]")
        # chequePayableSelect.click()
        # time.sleep(1)
        # optionInChequePayableSelect = self.driver.find_element(By.XPATH, "//*[text() = 'Local']")
        # optionInChequePayableSelect.click()
        # time.sleep(1)
        #
        # chequeBankName = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeBankName']")
        # chequeBankName.send_keys('asjdhfjasflh')
        #
        # chequeMicrFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeMicr']")
        # chequeMicrFill.send_keys('123456789')
        #
        # radioChequeRenewal = self.driver.find_element(By.XPATH, "//*[@for='renewalCheque']")
        # radioChequeRenewal.click()
        # print("Cheque Selected.")

        buttonSave = self.driver.find_element(By.XPATH, "//*[text()='Save']")
        buttonSave.click()
        print("Save button clicked.")


        # time.sleep(5)
        # self.driver.quit()


auto=mProAutomate()
auto.loginFunctionality()
auto.selectPlan()
# auto.goalCalculator()
auto.illustration()
auto.mPROStepOne()
auto.mPROStepTwo()
auto.mPROStepThree()
auto.mPROStepFour()
auto.mPROStepFive()