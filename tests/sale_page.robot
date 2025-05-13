*** Settings ***
Library    ../resources/browser_actions.py
Library    ../resources/product_actions.py
*** Variables ***
${URL}     https://magento.softwaretestingboard.com/

*** Test Cases ***
Open Page And Click Men Category
    Open Chrome With Manager    ${URL}
    Click Men Category
    Set Implicit Wait           5
    Close Browser