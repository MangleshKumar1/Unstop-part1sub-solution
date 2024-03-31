from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://example.com/table')

# Find the table element
table = driver.find_element_by_css_selector('table')

# Get the column headers
headers = [header.text for header in table.find_elements_by_css_selector('theader')]


# Get the data rows
rows = []
for row in table.find_elements_by_css_selector('trow'):
    rows.append([cell.text for cell in row.find_elements_by_css_selector('tdata')])

# Print the headers
print(headers)

# Iterate over the rows and print each row
for row in rows:
    print(row)

driver.quit()