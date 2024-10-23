'''from schedule_job.scheduler import job
from api.config.settings import INTERVAL

if __name__ == "__main__":
    print(f"Starting weather monitoring every {INTERVAL // 60} minutes...")
    job()  # This will trigger the scheduler and data collection

from schedule_job.scheduler import job
from api.config.settings import INTERVAL
import schedule
import time

if __name__ == "__main__":
    print(f"Starting weather monitoring every {INTERVAL // 60} minutes...")

    # Schedule the job at the specified interval
    schedule.every(INTERVAL).seconds.do(job)

    try:
        while True:
            schedule.run_pending()  # This runs the scheduled jobs when their time comes
            time.sleep(1)  # Sleep to prevent busy waiting
    except Exception as e:
        print(f"An error occurred: {e}")
'''


from api.config.settings import INTERVAL, DAILY_ROLLUP_INTERVAL, ALERT_CHECK_INTERVAL
from data.database import initialize_database
import schedule
import time

if __name__ == "__main__":
    # Initialize the database at the start
    initialize_database()

    print(f"Starting weather monitoring every {INTERVAL // 60} minutes...")

    # Schedule the weather data fetching job
    from schedule_job.scheduler import job, rollup_daily_summary
    from alerts.altering import check_thresholds
    from visualizations.visualize import plot_weather_summary

    
    schedule.every(INTERVAL).seconds.do(job)

    # Schedule the daily rollup job (once every day)
    schedule.every(DAILY_ROLLUP_INTERVAL).minutes.do(rollup_daily_summary)

    # Schedule the alerting job (check for alerts every few minutes)
    
    schedule.every(ALERT_CHECK_INTERVAL).minutes.do(check_thresholds)

    # Schedule the daily visualization job (e.g., once per day after the daily rollup)
    
    schedule.every(DAILY_ROLLUP_INTERVAL).minutes.do(plot_weather_summary)
    try:
        while True:
            schedule.run_pending()  # Runs the scheduled jobs when their time comes
            time.sleep(1)  # Sleep to prevent busy waiting
    except Exception as e:
        print(f"An error occurred: {e}")
