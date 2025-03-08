from page import Page

def test_page(browser):
    main_page = Page(browser)
    main_page.goto_site()
    main_page.setName("Nikita")
    main_page.setPassword("123")
    main_page.selectDrink("Milk")
    main_page.selectDrink("Coffee")
    main_page.selectColor("Yellow")
    main_page.scrollToAutomation()
    main_page.selectAutomation("yes")
    main_page.setEmail("example@gmail.com")
    main_page.setMessage()
    main_page.clickButton()
    main_page.checkMessageAlert()