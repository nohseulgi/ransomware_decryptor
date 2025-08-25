# ransomware_decryptor

Ryuk 랜섬웨어 복호화 시도 코드가 들어있습니다. <br>
<code>FLAG.txt.ryk</code> 파일을 대상으로 AES-256-CBC 복호화를 시도했지만, Ryuk 랜섬웨어 구조상 공격자의 RSA 개인키 없이는 복호화가 되지 않음을 확인했습니다.

## 실행 방법
### 1. Python 환경 준비 후 라이브러리 설치
```bash
   pip install pycryptodome
```
### 2. 코드 실행
```bash
   python decryption.py
```
### 3. 실행 결과 예시
```bash
   DECRYPTION FAIL: Data must be padded to 16 byte boundary in CBC mode
```
## 코드 설명
- <code>uuid_key</code> → 랜섬노트에 있던 Recovery Key
- <code>sha256</code> → 32바이트 키로 변환
- <code>AES.MODE_CBC</code> + <code>iv=0</code> 고정
- 복호화 후 <code>unpad()</code> 처리 시도 → 실패 (키 불일치 확인)
## 주의사항
- 실습 목적으로 작성된 코드입니다.
## 참고
- KISA, Ryuk 랜섬웨어 암호기능 분석 보고서
- JennyTheCode 블로그: [AES CBC 암호화/복호화 예제](https://jennythecode.tistory.com/887)
