from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

DATABASE = "gpu_data.db"


def connection_creation(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection
    except Error as e:
        print(e)
        return None


@app.route('/')
def main_page():
    return render_template('main-page.html')


@app.route('/info-page')
def info_page():
    return render_template('info-page.html')


@app.route('/gpu-page')
def gpu_page():

    query = "SELECT chip_manufacture, series, GPU, Vram, clockspeed_in_MHz, is_currently_manufactured, average_price_NZD, average_benchmark FROM sheet_gpu_data"
    connection = connection_creation(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('gpu-page.html', data=data_list)


if __name__ == '__main__':
    app.run()


@app.route('/NVIDIA-gpu-page')
def NVIDIA_PAGE():
    query = "SELECT chip_manufacture, series, GPU, Vram, clockspeed_in_MHz, is_currently_manufactured, average_price_NZD, average_benchmark FROM sheet_gpu_data WHERE chip_manufacture = 'NVIDIA' "
    connection = connection_creation(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('NVIDIA-gpu-page.html', data=data_list)

@app.route('/AMD-gpu-page')
def AMD_PAGE():
    query = "SELECT chip_manufacture, series, GPU, Vram, clockspeed_in_MHz, is_currently_manufactured, average_price_NZD, average_benchmark FROM sheet_gpu_data WHERE chip_manufacture = 'AMD' "
    connection = connection_creation(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('AMD-gpu-page.html', data=data_list)
