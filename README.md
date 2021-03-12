# Phishing-Website-Classifier

## The objective of this project is to identify Phishing websites, these websites will replicate as similar to legitimate websites, hence stealing of users inforation is at the high rate.

## DATA SET DESCRIPTION :
### index has 11055 unique values
            having_IPhaving_IP_Address contains:			[-1  1]
            URLURL_Length contains:			                [ 1  0 -1]
            Shortining_Service contains:			        [ 1 -1]
            having_At_Symbol contains:			            [ 1 -1]
            double_slash_redirecting contains:			    [-1  1]
            Prefix_Suffix contains:			                [-1  1]
            having_Sub_Domain contains:			            [-1  0  1]
            SSLfinal_State contains:		            	[-1  1  0]
            Domain_registeration_length contains:			[-1  1]
            Favicon contains:			                    [ 1 -1]
            port contains:			                        [ 1 -1]
            HTTPS_token contains:			                [-1  1]
            Request_URL contains:			                [ 1 -1]
            URL_of_Anchor contains:			                [-1  0  1]
            Links_in_tags contains:			                [ 1 -1  0]
            SFH contains:			                        [-1  1  0]
            Submitting_to_email contains:			        [-1  1]
            Abnormal_URL contains:			                [-1  1]
            Redirect contains:			                    [0 1]
            on_mouseover contains:			                [ 1 -1]
            RightClick contains:			                [ 1 -1]
            popUpWidnow contains:			                [ 1 -1]
            Iframe contains:			                    [ 1 -1]
            age_of_domain contains:			                [-1  1]
            DNSRecord contains:			                    [-1  1]
            web_traffic contains:			                [-1  0  1]
            Page_Rank contains:			                    [-1  1]
            Google_Index contains:			                [ 1 -1]
            Links_pointing_to_page contains:			    [ 1  0 -1]
            Statistical_report contains:			        [-1  1]
            Result contains:			                    [-1  1]
         
 
 According to the Data, "1,0,-1" represents,
    a. 1 means legitimate
    b. 0 is suspicious
    c. -1 is phishing
    
 DATA SPREAD
     1    6157
    -1    4898
    
 To use this source code :
    1. clone this repo
    2. First install requiremnts.txt file and before that ensure to create conda environment
    3. Then makesure the data is in loader module
    4. Run main.py file and with the built model future prediction can be done
    5. To do prediction download 'finalized_model.sav' 
