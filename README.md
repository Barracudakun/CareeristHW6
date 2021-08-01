echo # CareeristHW6
6.1 Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions
https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 

Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page 
 When Store original windows
 And Click on Amazon Privacy Notice link (*see image below)
 And Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 And User can close new window and switch back to original


6.2 (not required)  [Loops] Make a test case which:
Clicks on Best Sellers link on the top menu
Clicks on each top link and verify that new page opens

# info 
Store original window and all old windows:
original_window = driver.current_window_handle
old_windows = driver.window_handles
Click on element that is supposed to open a new window:
element.click()
Wait for new window to open:
driver.wait.until(EC.new_window_is_opened)
Switch to new window:
new_window = driver.window_handles[1]
driver.switch_to_window(new_window)
Close new window:
driver.close()
And return back:
driver.switch_to_window(original_window)
