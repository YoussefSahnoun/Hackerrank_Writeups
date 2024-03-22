def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles_in_sight=[]
    for obstacle in obstacles:
        if obstacle[0]==r_q or obstacle[1]==c_q or abs(obstacle[0]-r_q)==abs(obstacle[1]-c_q):
            obstacles_in_sight.append(obstacle)
    print(obstacles_in_sight)
    closest_right=n-c_q
    closest_left=c_q-1
    closest_up=n-r_q
    closest_down=r_q-1
    if (r_q,c_q)!= (1,n) and (r_q,c_q) != (n,1):
        
        closest_diag1_up=sum([1 for i in range(1,n) if r_q+i <=n and  c_q+i <= n])
        closest_diag1_down=sum([1 for i in range(1,n) if r_q-i >=1 and  c_q-i >= 1])
    else:
        closest_diag1_up=0
        closest_diag1_down=0
        
    if (r_q,c_q) != (1,1) and (r_q,c_q) != (n,n):
        closest_diag2_up=sum([1 for i in range(1,n) if r_q+i <=n and  c_q-i >= 1])
        closest_diag2_down=sum([1 for i in range(1,n) if r_q-i >=1 and  c_q+i <= n])
    else:
        closest_diag2_up=0
        closest_diag2_down=0
        
    for obstacle in obstacles_in_sight:
        if obstacle[0]>r_q and obstacle[1]==c_q and obstacle[0]-r_q <= closest_up:
            closest_up=obstacle[0]-r_q-1
        if obstacle[0]<r_q and obstacle[1]==c_q and r_q-obstacle[0] <= closest_down:
            closest_down=r_q-obstacle[0]-1
        if obstacle[1]>c_q and obstacle[0]==r_q and obstacle[1]-c_q <= closest_right:
            closest_right=obstacle[1]-c_q-1
        if obstacle[1]<c_q and obstacle[0]==r_q and c_q-obstacle[1] <= closest_left:
            closest_left=c_q-obstacle[1]-1
        if obstacle[0]>r_q and obstacle[1]>c_q and obstacle[0]-r_q <= closest_diag1_up:
            closest_diag1_up=obstacle[0]-r_q-1
        if obstacle[0]<r_q and obstacle[1]<c_q and  r_q-obstacle[0]<= closest_diag1_down:
            closest_diag1_down=r_q-obstacle[0]-1
        if obstacle[0]>r_q and obstacle[1]<c_q and obstacle[0]-r_q <= closest_diag2_up:
            closest_diag2_up=obstacle[0]-r_q-1
        if obstacle[0]<r_q and obstacle[1]>c_q and  r_q-obstacle[0]<= closest_diag2_down:
            closest_diag2_down=r_q-obstacle[0]-1
    
    return closest_right+closest_left+closest_up+closest_down+closest_diag1_up+closest_diag1_down+closest_diag2_up+closest_diag2_down