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
        self.wait = WebDriverWait(self.driver, 5000)
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
        # enterCustomerId.send_keys("29471")
        enterCustomerId.send_keys("626018")
        # kartik.bisaria@kelltontech.com

        fetchDetailsBtn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Fetch')]")
        fetchDetailsBtn.click()

        clickOnCross = self.driver.find_element(By.XPATH, "(//*[@d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'])[3]")
        clickOnCross.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='self']")))
        clickOnSelf= self.driver.find_element(By.XPATH, "//*[@for='self']")
        time.sleep(5)
        clickOnSelf.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='panNumber']")))
        panFill = self.driver.find_element(By.XPATH, "//*[@name='panNumber']")
        panFill.send_keys("CHGPD8457F")


        # time.sleep(30)
        #
        # btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        # btnProceed.click()

    def newApplicationFormOneStepTwo(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='alternateMobileNo']")))

        alternateMobileNumber= self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateMobileNumber.send_keys("9650479781")

        purposeOfInsuranceDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        purposeOfInsuranceDropdown.click()

        optionInInsuranceDropdown = self.driver.find_element(By.XPATH,"//*[contains(text(),'Retirement')]")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        lifeStageDropdown.click()

        optionInLifeStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married with children')]")
        optionInLifeStage.click()
        print("Single Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('900000')
        print("Gross Income Entered")

        existingPolicy = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[4]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Salaried']")
        optionInOccupation.click()
        print("Salaried Selected")
        time.sleep(2)

        recommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Monthly Income Advantage Plan']")
        optionInRecommendProduct.click()
        print("Product Selected")

        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_12']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        policyTerm.click()
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_22']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        desireIncome = self.driver.find_element(By.XPATH, "//*[@for='desiredAnnualIncomeNo']")
        desireIncome.click()
        time.sleep(1)


        dividentAdjustment = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        dividentAdjustment.click()
        time.sleep(1)

        optionIndividentAdjustment = self.driver.find_element(By.XPATH, "//*[@id='liId_Compound Reversionary Bonus']")
        optionIndividentAdjustment.click()
        print("Dividend Selected")
        time.sleep(2)

        premiumCommitFill = self.driver.find_element(By.XPATH, "//*[@name='premiumCommitment']")
        premiumCommitFill.send_keys("90000")
        print("Sum Assured Filled")
        time.sleep(1)

        riderADDDetails = self.driver.find_element(By.XPATH, "//*[@name='isAccidentalDeathAndDismembermentRider']")
        riderADDDetails.click()
        time.sleep(1)

        enterADDrider = self.driver.find_element(By.XPATH, "//*[@name='accidentalDeathAddAmount']")
        enterADDrider.send_keys("50000")

        riderCovidetails = self.driver.find_element(By.XPATH, "//*[@name='isCOVID19OneYearTermRider']")
        riderCovidetails.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[2]")))
        buttonNo = self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[2]")
        buttonNo.click()
        time.sleep(2)
        enterCovid = self.driver.find_element(By.XPATH, "//*[@name='covidSumAssured']")
        enterCovid.send_keys("100000")
        time.sleep(1)

        Termrider = self.driver.find_element(By.XPATH, "//*[@name='isTermPlusRider']")
        Termrider.click()
        print("Term selected")
        time.sleep(1)
        enterTermrider = self.driver.find_element(By.XPATH, "//*[@name='termPlusAddAmount']")
        enterTermrider.send_keys("50000")
        time.sleep(1)
        riderTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        riderTerm.click()
        time.sleep(1)
        optionInRiderTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_12']")
        optionInRiderTerm.click()

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(8)

        self.driver.switch_to_window(windowBefore)

    def newApplicationFormOneStepThree(self):

        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Raj Kumari")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Mohammad Maji")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Single Selected")

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Post Graduate')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Others')])[2]")
        optionInIndustrySelect.click()
        print("Industry Selected")

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Society']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        organisationFill.send_keys("ORG")

        preferredLanguage = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Gujarati']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='accountNumber21']")))
        buttonNomniee = self.driver.find_element(By.XPATH, "//*[@for='accountNumber21']")
        buttonNomniee.click()
        print("Nominee Selected.")
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='NA']")))
        calendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        calendarNomineeFill.click()

        yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearNomineeSel = Select(yearNomineeDropdown)
        yearNomineeSel.select_by_value('2002')

        monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthNomineeSel = Select(monthNomineeDropdown)
        monthNomineeSel.select_by_value('0')

        dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-16']")
        dateNomineeSel.click()

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Female')]")
        genderSelected.click()
        print("Gender Clicked")

        relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[8]")
        relationshipProposer.click()
        time.sleep(1)
        optionInRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Sister']")
        optionInRelationshipProposer.click()
        print("Relationship Sister Selected.")
        time.sleep(1)



    def newApplicationFormOneStepFour(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(text(), 'No')])[6]")))

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
        weightFill.send_keys("56")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Cancel')]")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")

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
auto.newApplicationFormOneStepFive()
