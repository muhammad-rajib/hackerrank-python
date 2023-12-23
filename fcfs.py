# FCFS: First Come First Serve Scheduling Algorithm

ARRIVAL_COL = 0
CPU_TIME_COL = 1
EXECUTION_COL = 2
WAITING_COL = 3
TAT_COL = 4  # TAT = Turn Around Time


def process_index(arrival_time_list, arrival_time):
    for i in range(len(arrival_time_list)):
        if arrival_time_list[i] == arrival_time:
            return i


def print_fcfs_table(fcfs_table):
    print("\nFirst Come First Server Table:")
    for row in fcfs_table:
        print(row)
    print('\n')

    total_waiting_time = 0
    total_tat = 0
    for i in range(len(fcfs_table)):
        print(f"Process {i+1}: Waiting Time: {fcfs_table[i][WAITING_COL]}  Turnaround Time: {fcfs_table[i][TAT_COL]}")
        total_waiting_time += fcfs_table[i][WAITING_COL]
        total_tat += fcfs_table[i][TAT_COL]

    print('\nAverage Waiting Time:', total_waiting_time / len(fcfs_table))
    print('Average Turnaround Time:', total_tat / len(fcfs_table))
    print('\n')

def fcfs_algorithm(fcfs_table, total_process):
    arrival_time_list = []
    for i in range(total_process):
        arrival_time_list.append(fcfs_table[i][ARRIVAL_COL])

    sorted_arrival_times = sorted(arrival_time_list)

    # Execution Time
    is_p1 = True
    for arri in sorted_arrival_times:
        arri_index = process_index(arrival_time_list, arri)
        if is_p1:
            fcfs_table[arri_index][EXECUTION_COL] = fcfs_table[arri_index][ARRIVAL_COL] + fcfs_table[arri_index][CPU_TIME_COL]
            is_p1 = False
        else:
            fcfs_table[arri_index][EXECUTION_COL] = fcfs_table[arri_index-1][EXECUTION_COL] + fcfs_table[arri_index][CPU_TIME_COL]

    # Waiting Time: W = ExecutionEndTime - (Arrival + CPUTime)
    for indx in range(total_process):
        fcfs_table[indx][3] = fcfs_table[indx][EXECUTION_COL] - (fcfs_table[indx][ARRIVAL_COL] + fcfs_table[indx][CPU_TIME_COL])
    
    # Turn Around Time or TAT: CPUTIme + WaitingTime
    for indx in range(total_process):
        fcfs_table[indx][TAT_COL] = fcfs_table[indx][CPU_TIME_COL] + fcfs_table[indx][WAITING_COL]

    print_fcfs_table(fcfs_table=fcfs_table)


if __name__ == '__main__':
    total_process = int(input('Enter the number of process: '))

    fcfs_table = []
    for i in range(total_process):
        fcfs_table.append([0]*5)
       
    print('Enter the CPU times: ')
    for i in range(total_process):
        j = i
        cpu_time = int(input(f"P{j+1}: "))
        fcfs_table[i][1] = cpu_time

    print('Enter the Arrival times: ')
    for i in range(total_process):
        j = i
        arrival_time = int(input(f"P{j+1}: "))
        fcfs_table[i][0] = arrival_time

    fcfs_algorithm(fcfs_table, total_process)
