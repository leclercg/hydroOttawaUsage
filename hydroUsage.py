import requests
import json
import time
import xmltodict
import datetime
from bs4 import BeautifulSoup
import secret

loginUrl = ('https://api.loginradius.com/identity/v2/auth/login?apiKey=d842e884-2dfb-4c8f-a971-f9eacf8e9f54&loginUrl=&emailTemplate=Verification English&verificationUrl=https://account.hydroottawa.com/login')
authenticatorUrl = ('https://account.hydroottawa.com/ajax/authenticator')
secureUrl = ('https://account.hydroottawa.com/')
downloadDataUrl = ('https://secure.hydroottawa.com/Usage/Secure/TOU/DownloadMyData.aspx')
ssoMhlUrl = ('https://account.hydroottawa.com/ajax/sso_mhl')
ssoTargetUrl = ('https://secure.hydroottawa.com/Usage/SSO/SSOTarget.aspx')

jsonPayload = {
    'email': secret.email,
    'password': secret.password
}
headersPayloadOptions = {
    'referrer': secureUrl,
    'origin': secureUrl,
    'Access-Control-Request-Method': 'POST',
    'Connection': 'keep-alive'
}
headersPayload = {
    'referrer': secureUrl,
    'origin': secureUrl,
    'Connection': 'keep-alive',
    'Content-Type': 'application/json'
}

with requests.session() as s:
    r = s.get(secureUrl)
    print('get: ', r)
    r = s.options(loginUrl, headers=headersPayloadOptions)
    print('options: ', r)
    r = s.post(loginUrl, json=jsonPayload, headers=headersPayload)
    print('login post: ', r)
    responseJson = r.json()
    payload = {
        'source': 'login',
        'uid': responseJson['Profile']['Uid'],
        'token': responseJson['access_token'],
        'expires': responseJson['expires_in'],
        'profile[Identities]': responseJson['Profile']['Identities'],
        'profile[Password]': responseJson['Profile']['Password'],
        'profile[LastPasswordChangeDate]': responseJson['Profile']['LastPasswordChangeDate'],
        'profile[PasswordExpirationDate]': responseJson['Profile']['PasswordExpirationDate'],
        'profile[LastPasswordChangeToken]': responseJson['Profile']['LastPasswordChangeToken'],
        'profile[EmailVerified]': responseJson['Profile']['EmailVerified'],
        'profile[IsActive]': responseJson['Profile']['IsActive'],
        'profile[IsDeleted]': responseJson['Profile']['IsDeleted'],
        'profile[Uid]': responseJson['Profile']['Uid'],
        'profile[CustomFields][EBilling]': responseJson['Profile']['CustomFields']['EBilling'],
        'profile[CustomFields][AccountID]': responseJson['Profile']['CustomFields']['AccountID'],
        'profile[CustomFields][PreviousBillAmount]': responseJson['Profile']['CustomFields']['PreviousBillAmount'],
        'profile[CustomFields][PreviousDueDate]': responseJson['Profile']['CustomFields']['PreviousDueDate'],
        'profile[IsEmailSubscribed]': responseJson['Profile']['IsEmailSubscribed'],
        'profile[UserName]': responseJson['Profile']['UserName'],
        'profile[NoOfLogins]': responseJson['Profile']['NoOfLogins'],
        'profile[PhoneId]': responseJson['Profile']['PhoneId'],
        'profile[PhoneIdVerified]': responseJson['Profile']['PhoneIdVerified'],
        'profile[Roles]': responseJson['Profile']['Roles'],
        'profile[ExternalUserLoginId]': responseJson['Profile']['ExternalUserLoginId'],
        'profile[RegistrationProvider]': responseJson['Profile']['RegistrationProvider'],
        'profile[IsLoginLocked]': responseJson['Profile']['IsLoginLocked'],
        'profile[LoginLockedType]': responseJson['Profile']['LoginLockedType'],
        'profile[LastLoginLocation]': responseJson['Profile']['LastLoginLocation'],
        'profile[RegistrationSource]': responseJson['Profile']['RegistrationSource'],
        'profile[IsCustomUid]': responseJson['Profile']['IsCustomUid'],
        'profile[UnverifiedEmail]': responseJson['Profile']['UnverifiedEmail'],
        'profile[IsSecurePassword]': responseJson['Profile']['IsSecurePassword'],
        'profile[PrivacyPolicy]': responseJson['Profile']['PrivacyPolicy'],
        'profile[ExternalIds]': responseJson['Profile']['ExternalIds'],
        'profile[IsRequiredFieldsFilledOnce]': responseJson['Profile']['IsRequiredFieldsFilledOnce'],
        'profile[ConsentProfile]': responseJson['Profile']['ConsentProfile'],
        'profile[PIN]': responseJson['Profile']['PIN'],
        'profile[RegistrationData]': responseJson['Profile']['RegistrationData'],
        'profile[ID]': responseJson['Profile']['ID'],
        'profile[Provider]': responseJson['Profile']['Provider'],
        'profile[Prefix]': responseJson['Profile']['Prefix'],
        'profile[FirstName]': responseJson['Profile']['FirstName'],
        'profile[MiddleName]': responseJson['Profile']['MiddleName'],
        'profile[LastName]': responseJson['Profile']['LastName'],
        'profile[Suffix]': responseJson['Profile']['Suffix'],
        'profile[FullName]': responseJson['Profile']['FullName'],
        'profile[NickName]': responseJson['Profile']['NickName'],
        'profile[ProfileName]': responseJson['Profile']['ProfileName'],
        'profile[BirthDate]': responseJson['Profile']['BirthDate'],
        'profile[Gender]': responseJson['Profile']['Gender'],
        'profile[Website]': responseJson['Profile']['Website'],
        'profile[Email][0][Type]': responseJson['Profile']['Email'][0]['Type'],
        'profile[Email][0][Value]': responseJson['Profile']['Email'][0]['Value'],
        'profile[Country]': responseJson['Profile']['Country'],
        'profile[ThumbnailImageUrl]': responseJson['Profile']['ThumbnailImageUrl'],
        'profile[ImageUrl]': responseJson['Profile']['ImageUrl'],
        'profile[Favicon]': responseJson['Profile']['Favicon'],
        'profile[ProfileUrl]': responseJson['Profile']['ProfileUrl'],
        'profile[HomeTown]': responseJson['Profile']['HomeTown'],
        'profile[State]': responseJson['Profile']['State'],
        'profile[City]': responseJson['Profile']['City'],
        'profile[Industry]': responseJson['Profile']['Industry'],
        'profile[About]': responseJson['Profile']['About'],
        'profile[TimeZone]': responseJson['Profile']['TimeZone'],
        'profile[LocalLanguage]': responseJson['Profile']['LocalLanguage'],
        'profile[CoverPhoto]': responseJson['Profile']['CoverPhoto'],
        'profile[TagLine]': responseJson['Profile']['TagLine'],
        'profile[Language]': responseJson['Profile']['Language'],
        'profile[Verified]': responseJson['Profile']['Verified'],
        'profile[UpdatedTime]': responseJson['Profile']['UpdatedTime'],
        'profile[Positions]': responseJson['Profile']['Positions'],
        'profile[Educations]': responseJson['Profile']['Educations'],
        'profile[PhoneNumbers]': responseJson['Profile']['PhoneNumbers'],
        'profile[IMAccounts]': responseJson['Profile']['IMAccounts'],
        'profile[Addresses]': responseJson['Profile']['Addresses'],
        'profile[MainAddress]': responseJson['Profile']['MainAddress'],
        'profile[Created]': responseJson['Profile']['Created'],
        'profile[CreatedDate]': responseJson['Profile']['CreatedDate'],
        'profile[ModifiedDate]': responseJson['Profile']['ModifiedDate'],
        'profile[ProfileModifiedDate]': responseJson['Profile']['ProfileModifiedDate'],
        'profile[LocalCity]': responseJson['Profile']['LocalCity'],
        'profile[ProfileCity]': responseJson['Profile']['ProfileCity'],
        'profile[LocalCountry]': responseJson['Profile']['LocalCountry'],
        'profile[ProfileCountry]': responseJson['Profile']['ProfileCountry'],
        'profile[FirstLogin]': responseJson['Profile']['FirstLogin'],
        'profile[IsProtected]': responseJson['Profile']['IsProtected'],
        'profile[RelationshipStatus]': responseJson['Profile']['RelationshipStatus'],
        'profile[Quota]': responseJson['Profile']['Quota'],
        'profile[Quote]': responseJson['Profile']['Quote'],
        'profile[InterestedIn]': responseJson['Profile']['InterestedIn'],
        'profile[Interests]': responseJson['Profile']['Interests'],
        'profile[Religion]': responseJson['Profile']['Religion'],
        'profile[Political]': responseJson['Profile']['Political'],
        'profile[Sports]': responseJson['Profile']['Sports'],
        'profile[InspirationalPeople]': responseJson['Profile']['InspirationalPeople'],
        'profile[HttpsImageUrl]': responseJson['Profile']['HttpsImageUrl'],
        'profile[FollowersCount]': responseJson['Profile']['FollowersCount'],
        'profile[FriendsCount]': responseJson['Profile']['FriendsCount'],
        'profile[IsGeoEnabled]': responseJson['Profile']['IsGeoEnabled'],
        'profile[TotalStatusesCount]': responseJson['Profile']['TotalStatusesCount'],
        'profile[Associations]': responseJson['Profile']['Associations'],
        'profile[NumRecommenders]': responseJson['Profile']['NumRecommenders'],
        'profile[Honors]': responseJson['Profile']['Honors'],
        'profile[Awards]': responseJson['Profile']['Awards'],
        'profile[Skills]': responseJson['Profile']['Skills'],
        'profile[CurrentStatus]': responseJson['Profile']['CurrentStatus'],
        'profile[Certifications]': responseJson['Profile']['Certifications'],
        'profile[Courses]': responseJson['Profile']['Courses'],
        'profile[Volunteer]': responseJson['Profile']['Volunteer'],
        'profile[RecommendationsReceived]': responseJson['Profile']['RecommendationsReceived'],
        'profile[Languages]': responseJson['Profile']['Languages'],
        'profile[Projects]': responseJson['Profile']['Projects'],
        'profile[Games]': responseJson['Profile']['Games'],
        'profile[Family]': responseJson['Profile']['Family'],
        'profile[TeleVisionShow]': responseJson['Profile']['TeleVisionShow'],
        'profile[MutualFriends]': responseJson['Profile']['MutualFriends'],
        'profile[Movies]': responseJson['Profile']['Movies'],
        'profile[Books]': responseJson['Profile']['Books'],
        'profile[AgeRange]': responseJson['Profile']['AgeRange'],
        'profile[PublicRepository]': responseJson['Profile']['PublicRepository'],
        'profile[Hireable]': responseJson['Profile']['Hireable'],
        'profile[RepositoryUrl]': responseJson['Profile']['RepositoryUrl'],
        'profile[Age]': responseJson['Profile']['Age'],
        'profile[Patents]': responseJson['Profile']['Patents'],
        'profile[FavoriteThings]': responseJson['Profile']['FavoriteThings'],
        'profile[ProfessionalHeadline]': responseJson['Profile']['ProfessionalHeadline'],
        'profile[ProviderAccessCredential]': responseJson['Profile']['ProviderAccessCredential'],
        'profile[RelatedProfileViews]': responseJson['Profile']['RelatedProfileViews'],
        'profile[KloutScore]': responseJson['Profile']['KloutScore'],
        'profile[LRUserID]': responseJson['Profile']['LRUserID'],
        'profile[PlacesLived]': responseJson['Profile']['PlacesLived'],
        'profile[Publications]': responseJson['Profile']['Publications'],
        'profile[JobBookmarks]': responseJson['Profile']['JobBookmarks'],
        'profile[Suggestions]': responseJson['Profile']['Suggestions'],
        'profile[Badges]': responseJson['Profile']['Badges'],
        'profile[MemberUrlResources]': responseJson['Profile']['MemberUrlResources'],
        'profile[TotalPrivateRepository]': responseJson['Profile']['TotalPrivateRepository'],
        'profile[Currency]': responseJson['Profile']['Currency'],
        'profile[StarredUrl]': responseJson['Profile']['StarredUrl'],
        'profile[GistsUrl]': responseJson['Profile']['GistsUrl'],
        'profile[PublicGists]': responseJson['Profile']['PublicGists'],
        'profile[PrivateGists]': responseJson['Profile']['PrivateGists'],
        'profile[Subscription]': responseJson['Profile']['Subscription'],
        'profile[Company]': responseJson['Profile']['Company'],
        'profile[GravatarImageUrl]': responseJson['Profile']['GravatarImageUrl'],
        'profile[ProfileImageUrls]': responseJson['Profile']['ProfileImageUrls'],
        'profile[WebProfiles]': responseJson['Profile']['WebProfiles'],
        'profile[PinsCount]': responseJson['Profile']['PinsCount'],
        'profile[BoardsCount]': responseJson['Profile']['BoardsCount'],
        'profile[LikesCount]': responseJson['Profile']['LikesCount'],
        'profile[SignupDate]': responseJson['Profile']['SignupDate'],
        'profile[LastLoginDate]': responseJson['Profile']['LastLoginDate'],
        'profile[PreviousUids]': responseJson['Profile']['PreviousUids']
    }
    print('Number of logins: ', responseJson['Profile']['NoOfLogins'])
    r = s.post(authenticatorUrl, data=payload)
    print('authenticator post: ', r)
    r = s.get(secureUrl)
    print('succesfully logged in')

    ssoMhlPayload = {
        'account': responseJson['Profile']['CustomFields']['AccountID'],
        'request_type': 'BILLING'
    }

    r = s.post(ssoMhlUrl, data=ssoMhlPayload)
    print('SSO: ', r)
    responseSsoMhlJson = r.json()

    ssoTargetPayload = {
        'authssotoken': responseSsoMhlJson['token']
    }
    r = s.post(ssoTargetUrl, data=ssoTargetPayload)
    print('SSO Target: ', r)

    r = s.get(downloadDataUrl)
    print('Download My Data: ', r)

    # TODO: Need to figure out how to read data
