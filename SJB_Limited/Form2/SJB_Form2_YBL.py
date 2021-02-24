from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

class mProAutomate:

    # Axis - 655393 | india@2020
    # YBL  - 718842 | mnyl@4321 | Customer ID-  29471, 47942, 616658 (222222)
    # DST  - 934384 | MNYL@2020
    # SPARC- 782058 | MNYL@2020
    # Agency- 447660| Mnyl@2020
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
        username.send_keys("718842")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("mnyl@4321")

        btnSign=self.driver.find_element(By.XPATH,"//*[contains(text(),'SIGN')]")
        btnSign.click()


        btnNewApp=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-current='page']")))
        print("Login Successful.")

    def newApplicationFormOneStepOne(self):


        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@href='/']")))
        btnNewApplication= self.driver.find_element(By.XPATH,"//*[@href='/']")
        btnNewApplication.click()

        enterCustomerId = self.driver.find_element(By.XPATH, "//*[@name='CustomerID']")
        # enterCustomerId.send_keys("11111111")
        enterCustomerId.send_keys("2468")
        time.sleep(1)
        # enterCustomerId.send_keys("29471")
        # kartik.bisaria@kelltontech.com

        fetchDetailsBtn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Fetch')]")
        fetchDetailsBtn.click()
        time.sleep(1)

        clickOnCross = self.driver.find_element(By.XPATH, "(//*[@d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'])[3]")
        clickOnCross.click()
        # kartik.bisaria@kelltontech.com

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='self']")))
        clickOnSelf= self.driver.find_element(By.XPATH, "//*[@for='dependent']")
        time.sleep(3)
        clickOnSelf.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='panNumber']")))
        panFill = self.driver.find_element(By.XPATH, "//*[@name='panNumber']")
        panFill.send_keys("EFLPK9876K")


        # time.sleep(30)
        #
        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()

    def newApplicationFormOneStepTwo(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='alternateMobileNo']")))

        alternateMobileNumber= self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateMobileNumber.send_keys("9650479781")

        # stdCode = self.driver.find_element(By.XPATH, "//*[@name='stdCode']")
        # stdCode.send_keys("011")

        ##############Life Insured Details################
        lifeToInsured = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'insurerName']")
        lifeToInsured.send_keys("Sumit")
        time.sleep(1)

        lifegenderSelected = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Female')])[2]")
        lifegenderSelected.click()
        print("Gender Clicked")
        time.sleep(1)

        lifecalendarFill = self.driver.find_element(By.XPATH, "//*[@name='insurerDateOfBirth']")
        lifecalendarFill.click()
        time.sleep(1)

        lifeyearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearSel = Select(lifeyearDropdown)
        # yearSel.select_by_value('1977')
        yearSel.select_by_value('1982')

        lifemonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(lifemonthDropdown)
        # monthSel.select_by_value('11')
        monthSel.select_by_value('1')

        # dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-22']")
        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-16']")
        dateSel.click()
        time.sleep(2)

        liferelationshipDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        liferelationshipDropdown.click()
        time.sleep(1)

        optionInLifeRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Wife']")
        optionInLifeRelationshipProposer.click()
        print("Relationship Father Selected.")
        time.sleep(1)
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        purposeOfInsuranceDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        purposeOfInsuranceDropdown.click()
        time.sleep(1)

        optionInInsuranceDropdown = self.driver.find_element(By.XPATH, "//*[contains(text(),'Protection')]")
        optionInInsuranceDropdown.click()
        print("Protection Selected")

        lifeStageDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        lifeStageDropdown.click()
        time.sleep(1)

        optionInLifeStage = self.driver.find_element(By.XPATH, "//*[@id='liId_Close to retirement or retired']")
        optionInLifeStage.click()
        print("Married Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('900000')
        print("Gross Income Entered")

        existingPolicy = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[4]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Professional']")
        optionInOccupation.click()
        print("Salaried Selected")
        time.sleep(2)

        recommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Select Another Product']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(1)

        productName = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        productName.click()
        time.sleep(1)
        optionInproductName = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Saral Jeevan Bima']")
        optionInproductName.click()
        print("Product Selected")
        time.sleep(1)

        premiumType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        premiumType.click()
        time.sleep(1)
        optionInpremiumType = self.driver.find_element(By.XPATH, "//*[@id='liId_Limited Pay']")
        optionInpremiumType.click()
        print("Premium Payment Selected")
        time.sleep(2)

        premiumPaymentType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        premiumPaymentType.click()
        time.sleep(1)
        # optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_32']")
        optionInpremiumPaymentType = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        optionInpremiumPaymentType.click()
        print("Policy Term Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        policyTerm.click()
        time.sleep(1)
        # optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_32']")
        optionInpolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_10']")
        optionInpolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        mode = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        mode.click()
        time.sleep(1)
        modeofPayment = self.driver.find_element(By.XPATH, "//*[@id='liId_Annual']")
        modeofPayment.click()
        print("Annual Selected")
        time.sleep(2)

        SAFill = self.driver.find_element(By.XPATH, "//*[@name='sumAssured']")
        SAFill.send_keys('2400000')
        print("SA Entered")
        SmokingHabit = self.driver.find_element(By.XPATH, "//*[@for='nosmoke']")
        SmokingHabit.click()
        time.sleep(1)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[1]")))
        buttonYes = self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[1]")
        buttonYes.click()

        time.sleep(8)

        self.driver.switch_to_window(windowBefore)

    def newApplicationFormOneStepThree(self):

        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Sumt")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Upadhyay")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Married Selected")

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Professional']")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Aviation/AirForce']")
        optionInIndustrySelect.click()
        print("Industry Selected")

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Trust']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        natureDuties = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[1]")
        natureDuties.click()
        time.sleep(1)

        # natureSelect = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        # natureSelect.click()
        # time.sleep(1)
        # optionInNatureSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Cargo Vessel']")
        # optionInNatureSelect.click()
        # print("Nature Selected")

        # organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        # organisationFill.send_keys("ORG")
        # time.sleep(1)

        preferredLanguage = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Hindi']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(2)

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("Mr. BALAJI SHANKAR")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("SBIN0000845")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("515002206")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(2)

        calendarFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccOpeningDate']")
        calendarFill.click()

        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-7']")
        dateSel.click()
        time.sleep(2)

        ###################Life To Insured #####################

        fatherName = self.driver.find_element(By.XPATH, "//*[@name='insurerFatherName']")
        fatherName.send_keys("Chotu")
        time.sleep(1)

        dobSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        dobSelect.click()
        time.sleep(2)
        optiondobSelect = self.driver.find_element(By.XPATH, "//*[@id ='liId_Aadhaar']")
        optiondobSelect.click()
        time.sleep(2)

        education = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        education.click()
        time.sleep(2)
        optioneducation = self.driver.find_element(By.XPATH, "//*[@id ='liId_Professional']")
        optioneducation.click()
        time.sleep(2)

        marital = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        marital.click()
        time.sleep(2)
        optionmarital = self.driver.find_element(By.XPATH, "//*[@id ='liId_Married']")
        optionmarital.click()
        time.sleep(2)

        natureDuties = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[1]")
        natureDuties.click()
        time.sleep(1)

        clickOnIndian = self.driver.find_element(By.XPATH, "//*[@for='in1']")
        clickOnIndian.click()


        industry = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        industry.click()
        time.sleep(1)
        optionindustry = self.driver.find_element(By.XPATH, "//*[@id ='liId_Defence']")
        optionindustry.click()
        time.sleep(1)

        org = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        org.click()
        time.sleep(1)
        optionorg = self.driver.find_element(By.XPATH, "//*[@id ='liId_Trust']")
        optionorg.click()
        time.sleep(1)

        nature = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        nature.click()
        time.sleep(1)
        optionnature = self.driver.find_element(By.XPATH, "//*[@id ='liId_Combat role']")
        optionnature.click()
        time.sleep(1)

        border= self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[3]")
        border.click()

        occupation = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[16]")
        occupation.click()
        time.sleep(1)
        optionoccupation = self.driver.find_element(By.XPATH, "//*[@id ='liId_Professional']")
        optionoccupation.click()
        time.sleep(1)

        annualIncome= self.driver.find_element(By.XPATH, "//*[@name='insurerAnnualIncome']")
        annualIncome.send_keys("800000")
        time.sleep(1)

        hazardous = self.driver.find_element(By.XPATH, "//*[@for='InsurerHazardousActivitiesNo']")
        hazardous.click()

        criminal = self.driver.find_element(By.XPATH, "//*[@for='InsurerCriminalChargesNo']")
        criminal.click()

        holiday = self.driver.find_element(By.XPATH, "//*[@for='insurerTravelOrResideAbroadNo']")
        holiday.click()

        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[17]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[18]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_6']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='insurerWeightInKgs']")
        weightFill.click()
        weightFill.send_keys("66")
        time.sleep(2)


        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(1)

    ################################


    def newApplicationFormOneStepFour(self):

        ############# Payor Details ################
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(text(),'Yes')])[1]")))

        payorDifferent = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Yes')])[1]")
        payorDifferent.click()
        time.sleep(1)

        payorName = self.driver.find_element(By.XPATH, "//*[@name='payorName']")
        payorName.send_keys("Sonam")
        time.sleep(1)

        payorDob = self.driver.find_element(By.XPATH, "//*[@name='payorDateOfBirth']")
        payorDob.click()
        time.sleep(1)

        payorDobDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        payorDobDropdownSel = Select(payorDobDropdown)
        payorDobDropdownSel.select_by_value('1991')

        payorDobDropdownSel = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        payorDobDropdownSelSel = Select(payorDobDropdownSel)
        payorDobDropdownSelSel.select_by_value('1')

        payordateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-14']")
        payordateSel.click()
        time.sleep(1)
        print("payor Date Select")

        payorAdd = self.driver.find_element(By.XPATH, "//*[@name='payorAddress']")
        payorAdd.send_keys("F  185 PANCHSHEEL MARG BEHINDBHAGARIA BHAWAN C")
        time.sleep(1)

        payorState = self.driver.find_element(By.XPATH, "//*[@name='payorState']")
        payorState.send_keys("DELHI")
        time.sleep(1)
        payorstateToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'DEL')]")
        payorstateToSel.click()
        time.sleep(1)
        print("State Filled")
        time.sleep(1)

        payorannualIncome = self.driver.find_element(By.XPATH, "//*[@name='payorAnnualIncome']")
        payorannualIncome.send_keys("500000")
        time.sleep(1)

        payorPANExist = self.driver.find_element(By.XPATH, "//*[@name='isPayorPANExist']")
        payorPANExist.click()
        time.sleep(1)

        # payorPAN = self.driver.find_element(By.XPATH, "//*[@name='payorPanNumber']")
        # payorPAN.send_keys("AKJPJ8800A")
        # time.sleep(1)

        payorRelationship = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[2]")
        payorRelationship.click()
        time.sleep(1)
        optionInpayorRelationship = self.driver.find_element(By.XPATH, "//*[@id='liId_Spouse']")
        optionInpayorRelationship.click()
        time.sleep(1)

        bankEnter = self.driver.find_element(By.XPATH, "//*[@name='payorBankAccountNo']")
        bankEnter.send_keys("3876839763")
        time.sleep(1)

        bankNameEnter = self.driver.find_element(By.XPATH, "//*[@name='payorBankName']")
        bankNameEnter.send_keys("SBI Bank")
        time.sleep(1)

        bankBranchEnter = self.driver.find_element(By.XPATH, "//*[@name='payorBankBranch']")
        bankBranchEnter.send_keys("New Delhi")
        time.sleep(1)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Cancel')]")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Payment')]")))
        paymentStep5 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Payment')]")
        paymentStep5.click()

    def newApplicationFormOneStepFive(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Payment')]")))
        paymentStep5= self.driver.find_element(By.XPATH, "//*[contains(text(),'Payment')]")
        paymentStep5.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='Cheque']")))
        radioCheque = self.driver.find_element(By.XPATH, "//*[@for='Cheque']")
        radioCheque.click()
        print("Cheque Selected.")

        chequeFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeNumber']")
        chequeFill.send_keys('1234567234')

        calendarSelect = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeDate']")
        calendarSelect.click()
        time.sleep(1)
        chequeDateSelect = self.driver.find_element(By.XPATH, "//*[text()='2']")
        chequeDateSelect.click()


        chequePayableSelect= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[2]")
        chequePayableSelect.click()
        time.sleep(1)
        optionInChequePayableSelect = self.driver.find_element(By.XPATH, "//*[text() = 'Local']")
        optionInChequePayableSelect.click()
        time.sleep(1)

        chequeBankName = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeBankName']")
        chequeBankName.send_keys('asjdhfjasflh')

        chequeMicrFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeMicr']")
        chequeMicrFill.send_keys('123456789')

        radioChequeRenewal = self.driver.find_element(By.XPATH, "//*[@for='ECS']")
        radioChequeRenewal.click()
        print("Cheque Selected.")


        raID= self.driver.find_element(By.XPATH, "(// *[@ tabindex='0'])[6]")
        raID.click()
        time.sleep(1)

        raIDValue = self.driver.find_element(By.XPATH, "//*[@id='liId_764878']")
        raIDValue.click()

        sourcingBranchCode = self.driver.find_element(By.XPATH, "//*[@id='sourcingBranchCode_idd']")
        sourcingBranchCode.send_keys("251")

        sourcingBranchCodeValue= self.driver.find_element(By.XPATH, "(// *[contains(text(), '251')])[2]")
        sourcingBranchCodeValue.click()

        buttonSave = self.driver.find_element(By.XPATH, "//*[text()='Save']")
        buttonSave.click()
        print("Save button clicked.")




auto=mProAutomate()
auto.loginFunctionality()
auto.newApplicationFormOneStepOne()
auto.newApplicationFormOneStepTwo()
auto.newApplicationFormOneStepThree()
auto.newApplicationFormOneStepFour()
# auto.newApplicationFormOneStepFive()
