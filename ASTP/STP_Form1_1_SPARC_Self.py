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
        self.driver.get("https://mprouat.maxlifeinsurance.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.wait = WebDriverWait(self.driver, 60)
        action = AC(self.driver)

    def loginFunctionality(self):

        username= self.driver.find_element(By.ID, "userId")
        username.send_keys("ABBBY6754")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("max@1234")

        btnSign=self.driver.find_element(By.XPATH,"//*[contains(text(),'SIGN')]")
        btnSign.click()


        btnNewApp=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-current='page']")))
        print("Login Successful.")

    def newApplicationFormOneStepOne(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@href='/']")))
        btnNewApplication= self.driver.find_element(By.XPATH,"//*[@href='/']")
        btnNewApplication.click()


        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='panNumber']")))
        panFill= self.driver.find_element(By.XPATH,"//*[@name='panNumber']")
        panFill.send_keys("APCPB1546B")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='mobileNumber']")))
        mobNumberFill= self.driver.find_element(By.XPATH,"//*[@name='mobileNumber']")
        mobNumberFill.send_keys("7042970921")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='email']")))
        emailFill = self.driver.find_element(By.XPATH, "//*[@name='email']")
        emailFill.send_keys("kartik.bisaria@kelltontech.com")

        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()

    def newApplicationFormOneStepTwo(self):

        windowBefore = self.driver.window_handles[0]
        print("Window Before=",windowBefore)

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='firstName']")))
        firstNameFill = self.driver.find_element(By.XPATH,"//*[@name='firstName']")
        firstNameFill.send_keys("Gambhira Singh")

        lastNameFill = self.driver.find_element(By.XPATH,"//*[@name='lastName']")
        lastNameFill.send_keys("Chanchal")

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Female')]")
        genderSelected.click()
        print("Gender Clicked")

        calendarFill= self.driver.find_element(By.XPATH,"//*[@name='dateOfBirth']")
        calendarFill.click()

        yearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearSel = Select(yearDropdown)
        yearSel.select_by_value('1985')

        monthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(monthDropdown)
        monthSel.select_by_value('3')

        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-10']")
        dateSel.click()
        time.sleep(2)

        houseNumberFill= self.driver.find_element(By.XPATH,"//*[@name='permanentHouseNo']")
        houseNumberFill.send_keys('House No. 23')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentRoadNo']")
        roadNumberFill.send_keys('Sector-9')

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCountry']")
        countryFill.send_keys('India')
        time.sleep(1)
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Ind')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='permanentState']")
        stateFill.send_keys('BIHAR')
        time.sleep(1)
        stateToSel=self.driver.find_element(By.XPATH, "//*[contains(text(),'BIHAR')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.send_keys('DARBHANGA')
        time.sleep(1)
        cityToSel= self.driver.find_element(By.XPATH, "//*[contains(text(),'DARBHANGA')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill= self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.send_keys('847233')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateNumberToFill.send_keys('7977412402')
        print("Alternate number Filled")
        time.sleep(1)

        proofDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        proofDropdown.click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='liId_Driving License']")))
        proofSel = self.driver.find_element(By.XPATH, "//*[@id='liId_Driving License']")
        proofSel.click()
        time.sleep(1)

        addProofEnter = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'proofNumber']")
        addProofEnter.send_keys("DL3SEL019734")
        time.sleep(1)

        LicenseFill = self.driver.find_element(By.XPATH, "//*[@name='proofExpiryDate']")
        LicenseFill.click()

        lyearlicense = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        lyearliceSel = Select(lyearlicense)
        lyearliceSel.select_by_value('2022')

        lmonthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        lmonthNomineeSel = Select(lmonthNomineeDropdown)
        lmonthNomineeSel.select_by_value('11')

        ldateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-31']")
        ldateNomineeSel.click()

        purposeOfInsuranceDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        purposeOfInsuranceDropdown.click()
        time.sleep(1)

        optionInInsuranceDropdown=self.driver.find_element(By.XPATH,"//*[contains(text(),'Protection')]")
        optionInInsuranceDropdown.click()
        print("Protection Selected")

        lifeStageDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        lifeStageDropdown.click()


        optionInLifeStage= self.driver.find_element(By.XPATH, "//*[@id='liId_Married with no children']")
        optionInLifeStage.click()
        print("Single Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('700000')
        print("Gross Income Entered")

        existingPolicy=self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[3]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Student']")
        optionInOccupation.click()
        print("Salaried Selected")
        time.sleep(2)

        recommendProduct= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        # optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Select Another Product']")
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Super Term Plan']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(2)

        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_30']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        policyTerm.click()
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_30']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        levelSA = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        levelSA.click()
        time.sleep(1)
        optionInSA = self.driver.find_element(By.XPATH, "//*[@id='liId_Level Sum Assured']")
        optionInSA.click()
        print("Level Selected")
        time.sleep(2)

        SAFill = self.driver.find_element(By.XPATH, "//*[@name='sumAssured']")
        SAFill.send_keys('10000000')
        print("SA Entered")

        SmokingHabit= self.driver.find_element(By.XPATH, "//*[@for='smoke']")
        SmokingHabit.click()
        time.sleep(1)

        dividentAdjustment = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        dividentAdjustment.click()
        time.sleep(1)

        optionIndividentAdjustment = self.driver.find_element(By.XPATH, "//*[@id='liId_No Adjustment']")
        optionIndividentAdjustment.click()
        print("Dividend Selected")
        time.sleep(2)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(1)

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[1]")))
        # buttonYes= self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[1]")
        # buttonYes.click()

        ########################### step 3 #############################
        time.sleep(8)

        self.driver.switch_to_window(windowBefore)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill= self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Father")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Mother")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Single Selected")
        time.sleep(1)

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Diploma')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Merchant Marine/Navy']")
        optionInIndustrySelect.click()
        print("Industry Selected")
        time.sleep(1)

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Public Ltd']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        vesselSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        vesselSelect.click()
        time.sleep(1)
        optionInvesselSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Passenger/Ferry']")
        optionInvesselSelect.click()
        print("Organisation Selected")
        time.sleep(1)
        # organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        # organisationFill.send_keys("ORG")

        preferredLanguage= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[7]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Kannada']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        organisationFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeName']")
        organisationFill.send_keys("Sanjana Singh Chanchal")

        calendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        calendarNomineeFill.click()

        yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearNomineeSel = Select(yearNomineeDropdown)
        yearNomineeSel.select_by_value('1987')

        monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthNomineeSel = Select(monthNomineeDropdown)
        monthNomineeSel.select_by_value('11')

        dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-30']")
        dateNomineeSel.click()

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Female')]")
        genderSelected.click()
        print("Gender Clicked")

        relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[9]")
        relationshipProposer.click()
        time.sleep(1)
        optionInRelationshipProposer= self.driver.find_element(By.XPATH, "//*[@id ='liId_Sister']")
        optionInRelationshipProposer.click()
        print("Relationship Wife Selected.")
        time.sleep(2)

        # childName= self.driver.find_element(By.XPATH, "//*[@name='nomineeChildName']")
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



        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("NameName")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("SBIN0000845")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("515002206")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(2)

        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()
        time.sleep(5)

    def newApplicationFormOneStepFour(self):

        EIAyes= self.driver.find_element(By.XPATH, "//*[@for='politicallypower3']")
        EIAyes.click()
        time.sleep(1)

        OpenYes = self.driver.find_element(By.XPATH, "//*[@for='QA2New']")
        OpenYes.click()
        time.sleep(1)

        preferred= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        preferred.click()
        time.sleep(1)
        preferredSelect = self.driver.find_element(By.XPATH, "//*[@id ='liId_Karvy Insurance Repository Limited']")
        preferredSelect.click()
        time.sleep(1)

        spouseOccupation = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        spouseOccupation.click()
        time.sleep(1)
        optionspouseOccupation = self.driver.find_element(By.XPATH, "//*[@id ='liId_Self Employed']")
        optionspouseOccupation.click()
        time.sleep(1)

        enterSalary = self.driver.find_element(By.XPATH, "//*[@name='spouseAnnualIncome']")
        enterSalary.send_keys("200000")
        time.sleep(1)

        enterTotal = self.driver.find_element(By.XPATH, "//*[@name='spouseTotalInsuranceCover']")
        enterTotal.send_keys("1000000")
        time.sleep(1)


        hazardousActivitiesSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[6]")
        hazardousActivitiesSelect.click()

        criminalSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[7]")
        criminalSelect.click()

        travelSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[8]")
        travelSelect.click()

        travelSelect1 = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[9]")
        travelSelect1.click()

        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[8]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[9]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='weight']")
        weightFill.click()
        weightFill.send_keys("60")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Cancel')]")))

        clickCancel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Cancel')]")
        clickCancel.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popupProceed']")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")
        time.sleep(2)

    def newApplicationFormOneStepFive(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Payment')]")))
        paymentStep5= self.driver.find_element(By.XPATH, "//*[contains(text(),'Payment')]")
        paymentStep5.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='DemandDraft']")))
        radioCheque = self.driver.find_element(By.XPATH, "//*[@for='DemandDraft']")
        radioCheque.click()
        print("DD Selected.")

        chequeFill = self.driver.find_element(By.XPATH, "//*[@name='paymentDemandDraftNumber']")
        chequeFill.send_keys('1234567234')

        calendarSelect = self.driver.find_element(By.XPATH, "//*[@name='paymentDemandDraftDate']")
        calendarSelect.click()
        time.sleep(1)
        chequeDateSelect = self.driver.find_element(By.XPATH, "//*[text()='2']")
        chequeDateSelect.click()

        ddamount = self.driver.find_element(By.XPATH, "//*[@name='paymentDemandDraftAmount']")
        ddamount.send_keys("20650")

        chequePayableSelect = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[2]")
        chequePayableSelect.click()
        time.sleep(1)

        optionInChequePayableSelect = self.driver.find_element(By.XPATH, "//*[text() = 'Local']")
        optionInChequePayableSelect.click()
        time.sleep(1)

        ddBankName = self.driver.find_element(By.XPATH, "//*[@name='paymentDemandDraftBankName']")
        ddBankName.send_keys("SBI Bank")
        time.sleep(1)

        ddBankNameNumber = self.driver.find_element(By.XPATH, "//*[@name='paymentDemandDraftMicr']")
        ddBankNameNumber.send_keys("110002233")
        time.sleep(1)

        buttonSave = self.driver.find_element(By.XPATH, "//*[text()='Save']")
        buttonSave.click()
        print("Save button clicked.")


        # time.sleep(5)
        # self.driver.quit()


auto=mProAutomate()
auto.loginFunctionality()
auto.newApplicationFormOneStepOne()
auto.newApplicationFormOneStepTwo()
auto.newApplicationFormOneStepFour()
auto.newApplicationFormOneStepFive()