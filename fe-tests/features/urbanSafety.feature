Feature: CrimeStatPage

@explorenearbycommbtn
Scenario: Verify "Check Nearby Community" is clickable and Melbourne pedestrian and lighting map is visible
Given I open the home page
When I click the "Check Nearby Community" button
Then I should see the pedestrian & lighting page

@exploreNearbyCommCard
Scenario: Verify "Check Nearby Community" card is clickable and Melbourne pedestrian and lighting map is visible
Given I open the home page
When I click the "Discover more statistics" button
Then I click the "Check Nearby Community" button on the cards section
Then I should see the pedestrian & lighting page

@SafetyTipsSection
Scenario: Safety tips section is visible
Given I open the home page
When I click the "Check Nearby Community" button
Then I should see the pedestrian & lighting page
Then I should see the safety advice card
And I should see the first tip "Select area you plan to visit"
And I should see the second tip "Choose an area with a large flow of people"
And I should see the third tip "Avoid areas with poor lighting."

@Disclaimer
Scenario: Historical disclaimer is visible
Given I open the home page
When I click the "Check Nearby Community" button
Then I should see the pedestrian & lighting page
Then I should see the safety advice card
Then I should see historical disclaimer "Historical data does not indicate future, Please stay alert at any time"


