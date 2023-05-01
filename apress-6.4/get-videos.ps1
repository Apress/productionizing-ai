$account_id="YOUR-ACCOUNT-ID"
$api_key="YOUR-KEY"
$location="trial"
# NB to get your video ID, open in https://www.videoindexer.ai/ then select
# Insights (JSON) from the dropdown box beside "Download". Then search in the JSON
# for "videoid"
$videoId="YOUR-VIDEOID"

# Call the AccessToken method with the API key in the header to get an access token
#NEW
$token = Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/auth/$location/Accounts/$account_id/Videos/$videoId/AccessToken" -Headers @{'Ocp-Apim-Subscription-Key' = $api_key}
#OLD
#$token = Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/auth/$location/Accounts/$account_id/AccessToken" -Headers @{'Ocp-Apim-Subscription-Key' = $api_key}

# Use the access token to make an authenticated call to the Videos method to get a list of videos in the account
#Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/$location/Accounts/$account_id/Videos?accessToken=$token" | ConvertTo-Json

# Drill-down
#Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/$location/Accounts/$account_id/Videos/Search?accessToken=$token&id=$videoId" | ConvertTo-Json

#Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/$location/Accounts/$account_id/Videos/$videoId/InsightsWidget?accessToken=$token" | ConvertTo-Json

Invoke-RestMethod -Method "Get" -Uri "https://api.videoindexer.ai/$location/Accounts/$account_id/Videos/$videoId/Index?accessToken=$token" | ConvertTo-Json


