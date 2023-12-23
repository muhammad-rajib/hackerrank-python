def sjf_non_preemptive(num_processes, cpu_times, arrival_times):
    processes = []
    for i in range(num_processes):
        processes.append((f'P{i + 1}', cpu_times[i], arrival_times[i]))

    processes.sort(key=lambda x: (x[1], x[2]))

    # update process
    updated_process = []
    for val in processes:
        if val[2] == 0:
            updated_process.append(val)

    for val in processes:
        if val[2] != 0:
            updated_process.append(val)
        
    processes = updated_process
    
    # print sequence of process
    print('\n')
    for item in processes:
        print(f"{item}", end=" ---> ")
    print('\n')

    waiting_time = 0
    turnaround_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    # Calculate Waiting and Turnaround Time
    print(f"Process {processes[0][0]}: Waiting Time: {processes[0][2]} Turnaround Time: {processes[0][1]}")
    waiting_time = processes[0][2]
    turnaround_time = processes[0][1]
    total_waiting_time += waiting_time
    total_turnaround_time += turnaround_time
    execution_time = turnaround_time

    for inx in range(1, num_processes):
        waiting_time = execution_time - processes[inx][2]
        turnaround_time = waiting_time + processes[inx][1]
        execution_time = execution_time + processes[inx][1]
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        print(f"Process {processes[inx][0]}: Waiting Time: {waiting_time} Turnaround Time: {turnaround_time}")
        

    # Average Waiting and Turnaround Time
    average_waiting_time = total_waiting_time / num_processes
    average_turnaround_time = total_turnaround_time / num_processes
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


if __name__ == '__main__':
    num_processes_input = int(input("Enter the number of processes: "))
    print('\nEnter the CPU times: ')
    cpu_times_input = [int(input(f"CPU time for P{i + 1}: ")) for i in range(num_processes_input)]
    print('\nEnter the arrival times: ')
    arrival_times_input = [int(input(f"Arrival time for P{i + 1}: ")) for i in range(num_processes_input)]

    # Call Non-Preemptive SJF Scheduling function
    sjf_non_preemptive(num_processes_input, cpu_times_input, arrival_times_input)
