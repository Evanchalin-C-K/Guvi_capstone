class Locators:
    # forget password
    forget_password = "//div[contains(@class, 'forgot')]/p"
    username_textbox = "//input[@name='username']"
    reset_pwd_btn = "//button[contains(@type, 'submit')]"

    # Login
    username = "[name='username']"  # CSS Selector
    password = "[name*='pass']"  # CSS selector
    login_btn = "button"  # Tag name

    # Admin
    admin_locator = "ul>li:first-child"  # CSS Selector
    option = "//div[@class='oxd-topbar-body']/nav/ul/li/span"
    option_1 = "Nationalities"
    option_2 = "Corporate"
    option_3 = "Configuration "

    menu_locator = "//ul[@class='oxd-main-menu']/li/a//span"
