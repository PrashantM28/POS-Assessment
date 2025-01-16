# POS Malaysia API and UI Assessment  

This repository contains test automation scripts for POS Malaysia’s Shipping Rate Calculator, including:  
1. A **Postman collection** to test the API functionality.  
2. A **Selenium python script** to automate the UI functionality.  


## Files  

- `POS Malaysia Shipping Rate Calculator APIs.postman_collection.json`: Postman collection for API testing.  
- `pos_shipping_rate_calculator_ui_test.py`: Selenium script for UI testing.  


### Note:
During testing for Selenium UI automation, it was observed that the **India** option was not visible in the "To" country dropdown on the UI. As a workaround, the script was configured to select **Afghanistan** instead of India to proceed with the automation.
