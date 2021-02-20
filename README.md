# 설명
Automated-MaliciousURL-Analysis는 텔레그램, Malwares.com API를 활용하여 URL이 악성인지 아닌지 판단해주는 스크립트입니다. 실행 후 텔레그램에 질의하고 싶은 URL을 입력하면 Malwares.com 질의 결과를 출력해줍니다. 사용자는 출력된 결과를 통해 URL의 악성여부를 판단할 수 있습니다.  

# 사용법
$ git clone https://github.com/mer1-97/Automated-MaliciousURL-Analysis.git

$ cd Automated-MaliciousURL-Analysis

$ pip install -r requirements.txt

$ 스크립트 실행전 해야할 일
* MalwaresAnalyze.py에 **self.api_key** = **'본인의 Malwares.com API Key'** 입력
* TelegramBot.py에 **self.user_id** = **'본인의 chat id'**, **self.token** = **'본인의 token'** 입력

$ python BotMalware.py

$ 텔레그램에 질의하고 싶은 URL 입력
