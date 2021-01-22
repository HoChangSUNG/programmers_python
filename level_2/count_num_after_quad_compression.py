answer = [0,0] # 0의 개수,1의 개수
def compression(arr,start_row,end_row,start_col,end_col):
    zero = 0
    one = 0
    if end_row - start_row == 1: # 더이상 쿼드를 압축할 수 없는 경우
        answer[arr[start_row][start_col]]+=1
        return
    for row in range(start_row,end_row): # 특정 영역 내부를 돌면서 확인
        for col in range(start_col,end_col):
            if arr[row][col] == 1:
                one+=1
            else:
                zero += 1
            if zero>0 and one>0: # 특정 영역 내부에 있는 수가 다를 경우
                compression(arr, start_row, (start_row + end_row) // 2, start_col, (start_col + end_col) // 2)  # 왼족 위
                compression(arr, start_row, (start_row + end_row) // 2, (start_col + end_col) // 2, end_col)  # 오른쪽 위
                compression(arr, (start_row + end_row) // 2, end_row, start_col, (start_col + end_col) // 2)  # 왼쪽 아래
                compression(arr, (start_row + end_row) // 2, end_row, (start_col + end_col) // 2, end_col)  # 오른쪽 아래
                return
    if zero>0 and one ==0: # 특정 영역 내부에 있는 수가 모두 0일 경우
        answer[0]+=1
        return
    elif zero==0 and one>0:# 특정 영역 내부에 있는 수가 모두 1일 경우
        answer[1] +=1
        return
def solution(arr): # 쿼드 압축 후 개수 세기
    compression(arr,0,len(arr),0,len(arr))
    return answer

arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))