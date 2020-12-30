from collections import deque
def  tree(skill,skill_tree): # 스킬 트리
    skill_queue = deque(list(skill))
    for sk in skill_tree :
        if skill_queue:
            if skill_queue[0] == sk :
                skill_queue.popleft()
            else :
                if sk in skill_queue :
                    return 0
        else :
            return 1
    return 1
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += tree(skill,skill_tree)
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill,skill_trees)