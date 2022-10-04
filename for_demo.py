#!/usr/bin/python
# -*- coding: utf-8 -*-
## 1. 초기 설정① #######################################
# 라이브러리 가져오기
from i611_MCS import *
from i611_extend import *
from i611_io import *

## 파일명은 무조건 영어!!
# 딜레이 함수 선언
# sleep 이라는 함수를 사용하기 위해서는 time이라는 함수 선언 이후 사용
# as t를 이용하여 time을 사용할수 있는 변수 선언
import time as t


def main():

    ## 2. 초기 설정② ####################################
    # i611 로봇 생성자
    rb = i611Robot()
    # 좌표계의 정의
    _BASE = Base()
    # 로봇과 연결 시작 초기화
    rb.open()
    # I/O 입출력 기능의 초기화 (I/O 미사용시 생략 가능 )
    IOinit(rb)

    # 초기 동작전 원점으로 복귀 이후 동작 시작
    rb.home()

    # 반복(0부터 10000까지)
    for i in range(0, 10000):

        # 인사하는 동작
        # 총 동작 4번
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for d in range(1, 5):

            # 반복 하는 동안 반복하는 값(i)가 홀수일때 1축은 30, 짝수 일때 1축은 -30
            if(d % 2 == 1):
                a = 30
            else:
                a = -30

            ## 교시 포인트 설정 ######################
            j1 = Joint(a, -20, -80, 0, 0, 0)

            ## 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=30)  # ptp 30% , j(joint)는 ptp 권장
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.home()  # 원점
            rb.move(j1)  # ptp를 사용할때는 move 명령어 이용
            t.sleep(1)  # 1초 딜레이

            # 손흔들기 반복(0~3)
            # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
            for k in range(0, 3):

                ## 교시 포인트 설정 ######################
                j2 = Joint(a, -20, -80, 0, 0, 20)
                j3 = Joint(a, -20, -80, 0, 0, -20)

                ## 동작 조건 설정 ##################################
                # MotionParam 생성자에서 동작 조건 설정
                # jnt speed -> PTP / lin speed -> Line speed
                m = MotionParam(jnt_speed=30)  # ptp 30%, j(joint)는 ptp 권장
                # MotionParam 형으로 동작 조건 설정
                rb.motionparam(m)

                ## 로봇 동작을 정의 ##############################
                # 작업 시작
                rb.move(j2, j3)  # ptp를 사용할때는 move 명령어 이용

        # 춤추기 첫번째 동작 =1
        # 반복(0~2)
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for x in range(0, 7):
            ## 3. 교시 포인트 설정 ######################
            j4 = Joint(0, 20, -40, 0, -90, 0)
            j5 = Joint(0, 18, -37, 0, -86, 0)

            ## 4. 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=40)  # ptp 40%, j(joint)는 ptp 권장
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 5. 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.move(j4, j5)

        # 춤추기 첫번째 동작 -2
        # 반복(0~2)
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for w in range(0, 7):
            ## 3. 교시 포인트 설정 ######################
            j6 = Joint(20, 20, -40, 0, -90, 0)
            j7 = Joint(20, 18, -37, 0, -86, 0)

            ## 4. 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=40)  # ptp 40%, j(joint)는 ptp 권장
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 5. 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.move(j6, j7)  # ptp를 사용할때는 move 명령어 이용

        # 춤추기 첫번째 동작 -3
        # 반복(0~2)
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for b in range(0, 7):
            ## 3. 교시 포인트 설정 ######################
            j8 = Joint(-20, 20, -40, 0, -90, 0)
            j9 = Joint(-20, 18, -37, 0, -86, 0)

            ## 4. 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=40)  # ptp 40%, j(joint)는 ptp 권장
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 5. 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.move(j8, j9)

        # 춤추기 두번째 동작 -1
        # 반복(0~2)
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for c in range(0, 7):
            j10 = Joint(0, -12, -82, 0, 0, 0)
            j11 = Joint(0, -14, -78, 0, 0, 0)

            ## 4. 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=40)
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 5. 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.move(j10, j11)  # ptp를 사용할때는 move 명령어 이용

        # 춤추기 두번째 동작 -2
        # 반복(0~2)
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for e in range(0, 6):
            j12 = Joint(20, -12, -82, 0, 0, 0)
            j13 = Joint(20, -14, -78, 0, 0, 0)

            ## 4. 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=40)
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 5. 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.move(j12, j13)  # ptp를 사용할때는 move 명령어 이용

        # 춤추기 두번째 동작 -3
        # 반복(0~2)
        # for의 값을 선언할때는 1부터 시작, 이외에는 0부터 시작
        for f in range(0, 6):
            j14 = Joint(-20, -12, -82, 0, 0, 0)
            j15 = Joint(-20, -14, -78, 0, 0, 0)

            ## 4. 동작 조건 설정 ##################################
            # MotionParam 생성자에서 동작 조건 설정
            # jnt speed -> PTP / lin speed -> Line speed
            m = MotionParam(jnt_speed=40)
            # MotionParam 형으로 동작 조건 설정
            rb.motionparam(m)

            ## 5. 로봇 동작을 정의 ##############################
            # 작업 시작
            rb.move(j14, j15)  # ptp를 사용할때는 move 명령어 이용

        ## 3. 교시 포인트 설정 ######################
        # j16 = Joint(0, 12, -90, 180, -180, 0)
        # j17 = Joint(0, 12, -90, -180, 180, 0)
        # j18 = Joint(90, 12, -90, 0, 0, 0)
        # j19 = Joint(90, 12, -90, 180, -180, 0)
        # j20 = Joint(90, 12, -90, -180, 180, 0)
        # j21 = Joint(-90, 12, -90, 0, 0, 0)
        # j22 = Joint(-90, 12, -90, 180, -180, 0)
        # j23 = Joint(-90, 12, -90, -180, 180, 0)

        # ## 4. 동작 조건 설정 ##################################
        # # MotionParam 생성자에서 동작 조건 설정
        # # jnt speed -> PTP / lin speed -> Line speed
        # m = MotionParam(jnt_speed=40)  # ptp 10% , j(joint)는 ptp 권장
        # # MotionParam 형으로 동작 조건 설정
        # rb.motionparam(m)

        # # ## 5. 로봇 동작을 정의 ##############################
        # # # 작업 시작
        # rb.move(j16, j17, j18, j19, j20, j21, j22, j23)

        # # 4번
        # for f in range(0, 5):
        #     j24 = Joint(-90, -12, 12, -90, -90, 90)
        #     j25 = Joint(-90, 12, -12, 90, -90, -90)

        #     ## 4. 동작 조건 설정 ##################################
        #     # MotionParam 생성자에서 동작 조건 설정
        #     # jnt speed -> PTP / lin speed -> Line speed
        #     m = MotionParam(jnt_speed=40)
        #     # MotionParam 형으로 동작 조건 설정
        #     rb.motionparam(m)

        #     ## 5. 로봇 동작을 정의 ##############################
        #     # 작업 시작
        #     rb.move(j24, j25)  # ptp를 사용할때는 move 명령어 이용

        # # 4번
        # for j in range(0, 5):
        #     j26 = Joint(90, -12, 12, -90, -90, 90)
        #     j27 = Joint(90, 12, -12, 90, -90, -90)

        #     ## 4. 동작 조건 설정 ##################################
        #     # MotionParam 생성자에서 동작 조건 설정
        #     # jnt speed -> PTP / lin speed -> Line speed
        #     m = MotionParam(jnt_speed=40)
        #     # MotionParam 형으로 동작 조건 설정
        #     rb.motionparam(m)

        #     ## 5. 로봇 동작을 정의 ##############################
        #     # 작업 시작
        #     rb.move(j26, j27)  # ptp를 사용할때는 move 명령어 이용

    ## 6. 종료 ######################################
    # 로봇과의 연결을 종료
    rb.close()


if __name__ == '__main__':
    main()
