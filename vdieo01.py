from selenium import webdriver











if __name__ == '__main__':
    url = 'https://36kr.com/p/732441733826692'
    driver = webdriver.Chrome()
    driver.get(url)
    name = driver.find_element_by_class_name('author-name ellipsis-1 active').text
    desc = driver.find_element_by_class_name('author-description').text
    title = driver.find_element_by_class_name('article-title margin-bottom-20 common-width').text
    data_time = driver.find_element_by_class_name('title-icon-item item-time').text
    content = driver.
