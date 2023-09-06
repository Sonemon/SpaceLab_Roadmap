from datetime import datetime, timedelta
import logging

#logging.basicConfig(level=logging.ERROR, encoding='utf-8')

def Get_newSchedule(days: int, work_days: int, rest_days: int, start_date: datetime):
    '''Получаем расписание для работника на заданное количество дней, чередуя рабочие и выходные от начала указанной даты'''
    try:
        result = []
        while days>0:
            for i in range(work_days):
                result.append(start_date)
                start_date+=timedelta(days=1)
                days-=1
            start_date+=timedelta(days=rest_days)
            days-=rest_days
        return result
    except Exception as e :
        logging.error(f"Error: {e}")
        return False
    
test_date = datetime(2020,1,30)
test_days = 5
test_work_days = 2
test_rest_days = 1
print(Get_newSchedule(test_days, test_work_days, test_rest_days, test_date))