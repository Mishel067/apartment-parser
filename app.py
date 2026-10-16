from flask import Flask, render_template
import sqlite3
import os
import logging
from parser_ import ToDataBase, Parser
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
DB_PATH = os.path.join(os.path.dirname(__file__), 'apartment.db')
app = Flask(__name__)

def update_database_job():
    logger.info('Trying to update database')
    try:
        url = 'https://www.nestpick.com/search/api/?city=dallas&order=relevance&currency=USD&location=101724385'
        parser = Parser(url).parse(5)
        if parser:
            with ToDataBase(DB_PATH, 'apartment') as db:
                db.to_db(parser)
            logger.info('Database updated successfully')
        else:
            logger.info('Database update failed')
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)

scheduler = BackgroundScheduler()
scheduler.add_job(update_database_job, 'interval', days=1)
scheduler.start()

@app.route('/')
def home():
    try:
        if not os.path.exists(DB_PATH):
            return "❌ Database file not found."

        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        apartments = conn.execute('SELECT * FROM apartment ORDER BY price ASC').fetchall()
        conn.close()

        if len(apartments) == 0:
            return "📭 Database is empty."

        return render_template('index.html', apartments=apartments)
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return f"❌ Error: {e}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
