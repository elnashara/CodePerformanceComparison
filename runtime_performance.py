from runtime_execution import RuntimeExecution 
import multiprocessing as mp
import statistics

class RuntimePerformance:
    def __init__(self, problem_number, function_param, sizes, versions, timeout):
        self.problem_number = problem_number
        self.function_param = function_param
        self.sizes = sizes
        self.versions = versions
        self.timeout = timeout

    def get_runtime(self, prompt_name, code_index, func_code):
        execution = RuntimeExecution(func_code, self.versions)
        p_result_list = []
        exception = 'N/A'
        for size in self.sizes:
            pool = mp.Pool(processes=1)  # Create a multiprocessing pool with 1 process
            lock = mp.Lock()  # Create a lock for synchronization
            print(f"\tTesting for list size {size}")
            time_list = []
            if exception == 'N/A':
                lock.acquire()  # Acquire the lock before running get_runtime
                async_result = pool.apply_async(execution.execute, args=(size, self.function_param,))  # Run get_runtime asynchronously
                try:
                    # time_out = self.timeout if self.best_avg_time == 'N/A' else min(self.timeout, self.best_avg_time * 200)
                    time_list, exception  = async_result.get(timeout=self.timeout)  # Get the result within timeout seconds
                except mp.TimeoutError:
                    exception = f"\t runtime.get_runtime terminated after {self.timeout} seconds"
                    timeout_counter = execution.get_timeout_counter()
                    print(f'timeout:{self.timeout}, timeout_counter: {timeout_counter}, exception: {exception}')
                    pool.terminate()  # Terminate the pool
                    time_list.append(self.timeout/timeout_counter)
                except Exception as e:
                    exception = f"\t exception: {e}"
                    print(exception)
                    pool.terminate()  # Terminate the pool
                    time_list.append(0)
                lock.release()  # Release the lock after funcA completes
            elif 'runtime.get_runtime' in exception:
                timeout_counter = execution.get_timeout_counter()
                print(f'timeout:{self.timeout}, timeout_counter: {timeout_counter}, exception: {exception}')
                time_list.append(self.timeout/timeout_counter)
            else:
                print(exception)
                time_list.append(0)
        
            min_time = min(time_list)
            avg_time = statistics.mean(time_list)
            # self.best_avg_time = avg_time if self.best_avg_time == 'N/A' else min(avg_time, self.best_avg_time)
            max_time = max(time_list)
            
            pool.close()
            pool.join()
            result = {
                'prompt_name': prompt_name,
                'code_segment': str(func_code),
                'code_index': code_index,
                'size': size,
                'min_time': min_time,
                'avg_time': avg_time,
                'max_time': max_time,
                'Exception': exception
            }
            # print(f"\t\t\tResult: {result} ")
            p_result_list.append(result)
        del execution
        return p_result_list
