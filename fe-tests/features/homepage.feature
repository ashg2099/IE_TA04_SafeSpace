Feature: Homepage

@websitelogo
Scenario: Verify SafeSpace logo is visible
  Given I open the home page
  Then I should see the SafeSpace logo

@discover
Scenario: Click discover button to scroll to crime statistics section
  Given I open the home page
  When I click the "Discover more statistics" button
  Then I should see the "See real crime stat" section

@welcometext
Scenario: Verify welcome section content
  Given I open the home page
  Then I should see the "Welcome to the SafeSpace" heading
  And I should see the welcome section description

@crimestatpage
Scenario: Click real crime stats button to navigate to crime statistics page
  Given I open the home page
  When I click the "Real crime stats" button
  Then I should see the statistics page