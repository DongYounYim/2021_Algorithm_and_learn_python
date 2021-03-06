# 기다리는걸 정말 싫어하는 '레오나'는 대출이 필요하여 은행에 방문하게 되었다.

# 앞에는 많은 사람(n)이 대기 중이며, 대기번호를 받고 한참 기다리던 '레오나'는

# 은행의 대기중인 손님의 수(n)는 알 수 있으나 대기번호들을 알 수 없어, 본인이 몇번 째 순서인지 알 수 없다.

# 그 때 은행에서 새로운 창구가 열리며 행원은 아래와 같이 말했다.

# "현재 손님 중, 대기번호가 앞에서 k번째 손님, 뒤에서 i번째 손님은 바로 와주시기 바랍니다."

# 은행에서 정렬되지 않은 대기번호 배열(WaitingList)을 공개한다. '레오나'는 이 대기번호 배열(WaitingList)을 확인하여 앞에서 k번째, 뒤에서 i번째 대기번호를 알아보고자 한다.

# 대기번호는 수가 작을 수록 우선순위가 높다

# 문제 : 주어지는 배열 WaitingList, n(손님 수), k, i를 활용하여, WaitingList 배열의 앞에서 k번째 값과 뒤에서 i번째 값의 합을 출력하시오.

# 입력값 범위

# 0 < n <= 100, 0 < k <= n, 0 < i <= n
# WaitingList : 1 이상, 1000이하의 자연수 n개로 구성된 배열
# 입력 예

# 10 2 4
# 18 26 24 28 7 23 9 27 25 21
# 출력 예

# 34


n, k, i= map(int, input().split())          #인자에 띄어쓰기 당 1개씩 int형으로 받는다
Waiting_list = list(map(int, input().split()))      #list형으로 형변환해서 받기
Waiting_list.sort()                         #배열 소팅

k_num = Waiting_list[k-1]                   #index가 0부터 시작하여 앞에서 k번째는 k-1 (k>0이라 가능)
i_num = Waiting_list[n-i]                   #뒤에서 i는 n-i
sum = k_num + i_num

print(sum)