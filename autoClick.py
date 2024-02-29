import pyautogui
import datetime
import time
import threading

# 전역 변수 설정
running = True

def click_at_center():
    # 화면의 가로, 세로 중앙 좌표 계산
    screenWidth, screenHeight = pyautogui.size()
    center_x = screenWidth // 2
    center_y = screenHeight // screenHeight

    # 마우스 커서 이동 및 클릭
    pyautogui.click(center_x, center_y)

def check_time(target_hour, target_minute):
    global running
    while running:
        # 현재 시간 가져오기
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # 설정한 시간이 되면 클릭 실행
        if current_hour == target_hour and current_minute == target_minute:
            click_at_center()

        # 1분마다 체크
        time.sleep(60)

def main(target_hour, target_minute):
    # 쓰레드 생성
    time_thread = threading.Thread(target=check_time, args=(target_hour, target_minute))
    time_thread.start()

    # 사용자 입력 대기
    input("프로그램을 종료하려면 엔터 키를 누르세요.\n")
    global running
    running = False

if __name__ == "__main__":
    # 설정할 시간 입력 받기
    target_hour = int(input("원하는 시간(24시간제)을 입력하세요 (0-23): "))
    target_minute = int(input("원하는 분을 입력하세요 (0-59): "))

    # 프로그램 실행
    main(target_hour, target_minute)
