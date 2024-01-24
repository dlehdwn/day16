from gtts import gTTS

text = "차번호 12마 3453 차주님 카운터로 와주세요"
tts = gTTS(text,lang='ko')
tts.save('result.mp3')