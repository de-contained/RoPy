import requests, os
import time

class RoPy:
      def __init__(
            self
      ):
          self.loginTime = time.time()
          self.loginTime

          self.headers = {
                 'authority'   : 'auth.roblox.com',
                 'dnt'         : '1',
                 'x-csrf-token': requests.post(
                                      "https://auth.roblox.com/v2/login"
                  ).headers[
                      'x-csrf-token'
                  ], 'sec-ch-ua-mobile': '?0',

                     'user-agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
                     'content-type'    : 'application/json;charset=UTF-8',
                     'accept'          : 'application/json, text/plain, */*',
          }

      def Login(
          self,
          roblo_security
      ):
          with requests.Session() as session:
               with session.get(
                    'https://api.roblox.com/currency/balance',
                    cookies = {
                            '.ROBLOSECURITY': str(roblo_security)
                    }
               ) as response:
                    if response.status_code in [
                       200,
                       201,
                       203,
                       204,
                    ]:
                       return True
                    else:
                       if __name__ == "__main__":
                          return False

      def robuxCheck(
          self,
          roblo_security
      ):
          with requests.Session() as session:
               with session.get(
                    'https://api.roblox.com/currency/balance',
                    cookies = {
                            '.ROBLOSECURITY': str(roblo_security)
                    }
               ) as response:
                    if response.status_code in [
                       200,
                       201,
                       203,
                       204,
                    ]:
                       return response.json()
                    else:
                       if __name__ == "__main__":
                          return response.json()
        
      def Register(
             self,
             user_name,
             pass_word,
             fun_captcha
      ):
          roblox_api = "https://auth.roblox.com/v2/signup"
          roblox_api

          with requests.Session() as session:
               with session.post(
                    roblox_api,
                    headers = self.headers,
                    json    = {
                             "username"                 :   user_name,
                             "password"                 :   pass_word,
                             "birthday"                 :   "08 Oct 2002",
                             "gender"                   :   1,
                             "isTosAgreementBoxChecked" :   True,
                             "context"                  :   "MultiverseSignupForm",
                             "referralData"             :   None,
                             "displayAvatarV2"          :   False,
                             "displayContextV2"         :   False,
                             "captchaId"                :   fun_captcha[0],
                             "captchaToken"             :   fun_captcha[1],
                             "captchaProvider"          :   "PROVIDER_ARKOSE_LABS",
                             "agreementIds"             :   [
                                                     "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3",
                                                     "848d8d8f-0e33-4176-bcd9-aa4e22ae7905"
                             ]
                  }
               ) as response:
                    if response.status_code in [
                       200,
                       201,
                       203,
                       204,
                    ]:
                       return response.json()
                    else:
                       if __name__ == "__main__":
                          return []
